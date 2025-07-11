# Decision Tree Classifier
Sử dụng thuật toán Decision Tree Classifier để tạo mô hình gợi ý phê duyệt khoản vay khách hàng của doanh nghiệp tài chính

# Bối cảnh giả định
Doanh nghiệp tài chính thường phải đối mặt với rủi ro liên quan tới các khoản tín dụng,
việc dự đoán rủi ro tín dụng là rất quan trọng để giảm thiểu tình trạng vỡ nợ và tối ưu hóa kết quả kinh doanh.

# Mục tiêu
Dự đoán liệu khách hàng có khả năng phải đối mặt với tình trạng vỡ nợ tín dụng hay không dựa trên dữ liệu nhân khẩu học, tài chính và hành vi. Dự đoán này sẽ hỗ trợ doanh nghiệp chủ động xác định các khách hàng có rủi ro cao và triển khai các biện pháp phòng ngừa phù hợp.

# Thông tin bộ dữ liệu
Bộ dữ liệu gồm 16 cột chứa các thông tin về nhân khẩu học, hành vi và tài chính khách hàng của doanh nghiệp, bộ dữ liệu đã được giản lược bớt một số thông tin để đảm bảo tính bảo mật thông tin của khách hàng <br/>
Giải thích ý nghĩa các cột thông tin trong bộ dữ liệu
<img width="1080" height="611" alt="Screenshot 2025-07-01 084245" src="https://github.com/user-attachments/assets/a1b709dc-4302-4114-9a30-30a5a81489d4" />
Thông tin trong bộ dữ liệu không bị thiếu hay bị lặp
<img width="370" height="471" alt="Screenshot 2025-07-11 214846" src="https://github.com/user-attachments/assets/fc239024-de4a-4e44-9794-ef70403e6220" /> <br/>
Một số thống kê cơ bản về giá trị trung bình, phân phối chuẩn, tứ phân vị hay các giá trị duy nhất, tấn suất xuất hiện bao nhiêu
<img width="718" height="462" alt="Screenshot 2025-07-11 214928" src="https://github.com/user-attachments/assets/f1c78f90-4a30-4804-a0c7-4a9a7d9a5158" />

# Xử lý dữ liệu
Dữ liệu trước khi đưa vào huấn luyện được xử lý về chuẩn hóa (Normalization), chuyển từ dạng category về các giá trị số tương ứng bằng phương pháp tương ứng (Ordinal hay One hot encoding), thực hiện xử lý cân bằng biến mục tiêu hoặc thêm một số cột mới để việc đào tạo mô hình được hiệu quả <br/>
Thực hiện xử lý cân bằng biến mục tiêu
<img width="1021" height="422" alt="Screenshot 2025-07-08 185816" src="https://github.com/user-attachments/assets/36d04214-a9ae-4955-80a0-4a95621e9b72" />
Bộ dữ liệu sau khi được xử lý
<img width="553" height="603" alt="Screenshot 2025-07-09 074558" src="https://github.com/user-attachments/assets/8a324f67-1118-45cc-b2f8-639e75c96af0" />
