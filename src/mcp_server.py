"""
MODEL CONTEXT PROTOCOL (MCP) SERVER MODULE
Mô phỏng kiến trúc MCP Server (Client-Server Architecture) cung cấp công cụ chuẩn hóa.
"""

import json
import sys
from typing import Dict, Any, List
from tools import TOOLS_SCHEMA, dispatch_tool_call

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class MCPStockServer:
    """
    Giả lập MCP Server tuân thủ chuẩn giao thức Model Context Protocol
    """
    def __init__(self, server_name: str = "ai-stock-broker-mcp-server"):
        self.server_name = server_name
        self.version = "2026.1.0"
        
    def list_tools(self) -> List[Dict[str, Any]]:
        """Trả về danh sách các Tools chuẩn giao thức MCP"""
        return TOOLS_SCHEMA
        
    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        [TASK 2.1] HỌC VIÊN HOÀN THIỆN HÀM THỰC THI TOOL TRÊN MCP SERVER
        Thực thi request gọi Tool theo chuẩn MCP JSON-RPC
        """
        res_str = dispatch_tool_call(tool_name, arguments)
        try:
            content = json.loads(res_str)
        except Exception:
            content = {"raw_result": res_str}
            
        return {
            "jsonrpc": "2.0",
            "server": self.server_name,
            "tool": tool_name,
            "result": content
        }


if __name__ == "__main__":
    print("==========================================================")
    print("KIỂM THỬ ĐỘC LẬP MCP SERVER (ai-stock-broker-mcp-server)")
    print("==========================================================")
    
    server = MCPStockServer()
    tools = server.list_tools()
    print(f"Khởi tạo thành công MCP Server: {server.server_name} (Version: {server.version})")
    print(f"Số lượng Tools công bố: {len(tools)}")
    
    sched_tool = next((t for t in tools if t.get("name") == "execute_trade_order"), None)
    if sched_tool and not sched_tool.get("parameters", {}).get("properties"):
        print("[TODO 1.2]: Tool 'execute_trade_order' chưa được định nghĩa properties trong 'src/tools.py'.")
    else:
        print("[TODO 1.2]: Tool 'execute_trade_order' đã có schema đầy đủ.")

    test_result = server.call_tool("analyze_stock_ticker", {"ticker": "FPT"})
    if not test_result:
        print("[TODO 2.1]: Hàm call_tool() đang trả về rỗng. Học viên hãy hoàn thiện TODO 2.1 trong 'src/mcp_server.py'!")
    else:
        print(f"[TODO 2.1]: Test dispatch tool 'analyze_stock_ticker' thành công:")
        print(f"   Phản hồi JSON-RPC: {json.dumps(test_result, ensure_ascii=False)}")
