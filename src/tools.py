"""
TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
  {
    "name": "analyze_stock_ticker",
    "description": "Tra cứu chỉ số tài chính và giá hiện tại của một mã cổ phiếu.",
    "parameters": {
      "type": "object",
      "properties": {
        "ticker": {
          "type": "string",
          "description": "Mã cổ phiếu cần tra cứu (ví dụ: 'FPT', 'VCB')"
        }
      },
      "required": ["ticker"]
    }
  },
  {
    "name": "execute_trade_order",
    "description": "Thực hiện lệnh mua hoặc bán cổ phiếu.",
    "parameters": {
      "type": "object",
      "properties": {
        "ticker": {
          "type": "string",
          "description": "Mã cổ phiếu cần giao dịch (ví dụ: 'FPT', 'VCB')"
        },
        "action": {
          "type": "string",
          "description": "Hành động giao dịch: 'MUA' hoặc 'BÁN'"
        },
        "volume": {
          "type": "integer",
          "description": "Khối lượng cổ phiếu (ví dụ: 1000)"
        },
        "target_price": {
          "type": "number",
          "description": "Giá mục tiêu cho một cổ phiếu (VNĐ)"
        }
      },
      "required": ["ticker", "action", "volume", "target_price"]
    }
  }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
  "FPT": {
    "company_name": "Công ty Cổ phần FPT",
    "current_price": 95000,
    "pe_ratio": 15.2,
    "eps": 6250,
    "volume": 2500000
  },
  "VCB": {
    "company_name": "Ngân hàng TMCP Ngoại thương Việt Nam",
    "current_price": 85000,
    "pe_ratio": 12.5,
    "eps": 6800,
    "volume": 1200000
  }
}


def execute_analyze_stock_ticker(ticker: str) -> str:
  """Thực thi tra cứu mã chứng khoán"""
  stock = MOCK_DATABASE.get(ticker.strip().upper())
  if stock:
    return json.dumps({
      "status": "SUCCESS",
      "ticker": ticker,
      "data": stock
    }, ensure_ascii=False)
  else:
    return json.dumps({
      "status": "NOT_FOUND",
      "message": f"Không tìm thấy dữ liệu cho mã cổ phiếu '{ticker}' trên sàn."
    }, ensure_ascii=False)


def execute_trade_order(ticker: str, action: str, volume: int, target_price: float) -> str:
  """Thực thi lệnh đặt mua/bán cổ phiếu"""
  return json.dumps({
    "status": "SUCCESS",
    "receipt_id": f"TR-{ticker}-{volume}-{int(target_price)}",
    "ticker": ticker.upper(),
    "action": action.upper(),
    "volume": volume,
    "price": target_price,
    "total_value": volume * target_price,
    "message": f"Đặt lệnh {action.upper()} thành công {volume} cổ phiếu {ticker.upper()} ở mức giá {target_price} VNĐ."
  }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
  "analyze_stock_ticker": execute_analyze_stock_ticker,
  "execute_trade_order": execute_trade_order
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
  """Hàm trung chuyển thực thi tool"""
  if tool_name in TOOL_ROUTER:
    try:
      return TOOL_ROUTER[tool_name](**arguments)
    except Exception as e:
      return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
  return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)


if __name__ == "__main__":
  print("==========================================================")
  print("KIỂM THỬ ĐỘC LẬP TOOL DISPATCHER (src/tools.py)")
  print("==========================================================")
  
  test_analyze = dispatch_tool_call("analyze_stock_ticker", {"ticker": "FPT"})
  print("Test dispatch 'analyze_stock_ticker':")
  print(f"  Response: {test_analyze}")
  
  test_trade = dispatch_tool_call("execute_trade_order", {
    "ticker": "FPT",
    "action": "MUA",
    "volume": 500,
    "target_price": 95000
  })
  print("Test dispatch 'execute_trade_order':")
  print(f"  Response: {test_trade}")
