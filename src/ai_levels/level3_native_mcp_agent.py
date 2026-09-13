"""
 [REFERENCE ONLY / CODE MẪU THAM KHẢO]
 CẤP ĐỘ 3: NATIVE MCP AGENT (Native Tool Calling + MCP Server Integration)
️ Lưu ý: File này chỉ dùng để đọc tham khảo kiến trúc. Không chỉnh sửa hay debug file này.
"""

import json

def get_weather(city: str) -> str:
  return f"Thời tiết {city}: 28°C, Nắng nhẹ."

def run_level3_demo():
  print("=== DEMO CẤP ĐỘ 3: NATIVE MCP AGENT ===")
  user_goal = "Tra cứu thông tin tài chính cổ phiếu FPT"
  print(f" Goal: {user_goal}")
  print(" [Thought]: Phát sinh Native Tool Call 'analyze_stock_ticker'...")
  print("️ [Native Tool Call]: analyze_stock_ticker({'ticker': 'FPT'})")
  print("️ [MCP Server Observation]: {'ticker': 'FPT', 'current_price': 95000, 'pe_ratio': 15.2}")
  print(" [Final Answer]: Cổ phiếu FPT hiện có giá 95.000 VNĐ, mức P/E là 15.2.")

if __name__ == "__main__":
  run_level3_demo()
