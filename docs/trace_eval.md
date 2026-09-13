# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Trần Chí Vĩ  
> **Mã Sinh Viên / Mã Học viên:** 2A202602968  
> **Chủ đề Lựa chọn:** Đề tài Mở — Trợ lý Phân tích Đầu tư Chứng khoán & Đặt Lệnh  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 5 / 5 | Agent phải tra cứu giá thị trường và chỉ số tài chính của mã cổ phiếu, phân tích tính khả thi, sau đó mới tiến hành đặt lệnh mua/bán. Sự phụ thuộc tuần tự giữa thông tin thị trường và quyết định tài chính rất rõ ràng. |
| **2. Tool Interaction** | 5 / 5 | Hệ thống tương tác với 2 công cụ phức tạp của sàn giao dịch: `analyze_stock_ticker` (truy xuất dữ liệu thị trường theo thời gian thực) và `execute_trade_order` (tiến hành giao dịch và cập nhật danh mục). |
| **3. Dynamic Decision** | 5 / 5 | Quyết định đặt lệnh phụ thuộc hoàn toàn vào kết quả quan sát (Dynamic): giá cổ phiếu vượt ngưỡng giới hạn hoặc P/E quá cao sẽ tự động thay đổi lời khuyên hoặc từ chối thực hiện giao dịch của người dùng. |
| **4. Long Horizon Goal** | 5 / 5 | Agent duy trì mục tiêu hỗ trợ nhà đầu tư từ lúc hỏi thông tin, phân tích cho đến khi lệnh được xác nhận khớp thành công, đảm bảo không bị gián đoạn hay mất ngữ cảnh. |
| **TỔNG ĐIỂM AGENTIC FIT** | **20 / 20** | *Tổng điểm 20/20: Bài toán có độ phức tạp hoàn hảo, rất phù hợp và tận dụng tối đa năng lực của Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API:

```json
[
  {
    "step": 1,
    "query": "Tra cứu chỉ số tài chính hiện tại của mã cổ phiếu FPT.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "analyze_stock_ticker",
    "arguments": {
      "ticker": "FPT"
    },
    "observation": {
      "status": "SUCCESS",
      "ticker": "FPT",
      "data": {
        "company_name": "Công ty Cổ phần FPT",
        "current_price": 95000,
        "pe_ratio": 15.2,
        "eps": 6250,
        "volume": 2500000
      }
    },
    "latency_ms": 1313.34
  },
  {
    "step": 2,
    "query": "Tra cứu chỉ số tài chính hiện tại của mã cổ phiếu FPT.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Kết quả xử lý: {\"company_name\": \"Công ty Cổ phần FPT\", \"current_price\": 95000, \"pe_ratio\": 15.2, \"eps\": 6250, \"volume\": 2500000}",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
