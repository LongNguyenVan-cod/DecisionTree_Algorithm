[decistion_tree.log](https://github.com/user-attachments/files/21201925/decistion_tree.log)# Decision Tree Classifier
Sử dụng thuật toán Decision Tree Classifier để tạo mô hình gợi ý phê duyệt khoản vay khách hàng của doanh nghiệp tài chính

# Context
Doanh nghiệp tài chính thường phải đối mặt với rủi ro liên quan tới các khoản tín dụng,
việc dự đoán rủi ro tín dụng là rất quan trọng để giảm thiểu tình trạng vỡ nợ và tối ưu hóa kết quả kinh doanh.

# Object
Dự đoán liệu khách hàng có khả năng phải đối mặt với tình trạng vỡ nợ tín dụng hay không dựa trên dữ liệu nhân khẩu học, tài chính và hành vi. Dự đoán này sẽ hỗ trợ doanh nghiệp chủ động xác định các khách hàng có rủi ro cao và triển khai các biện pháp phòng ngừa phù hợp.

# Dataset Information
Bộ dữ liệu gồm 16 cột chứa các thông tin về nhân khẩu học, hành vi và tài chính khách hàng của doanh nghiệp, bộ dữ liệu đã được giản lược bớt một số thông tin để đảm bảo tính bảo mật thông tin của khách hàng <br/>
Giải thích ý nghĩa các cột thông tin trong bộ dữ liệu
<img width="1080" height="611" alt="Screenshot 2025-07-01 084245" src="https://github.com/user-attachments/assets/a1b709dc-4302-4114-9a30-30a5a81489d4" />
<br/>
Thông tin trong bộ dữ liệu không bị thiếu hay bị lặp <br/>

<img width="370" height="471" alt="Screenshot 2025-07-11 214846" src="https://github.com/user-attachments/assets/fc239024-de4a-4e44-9794-ef70403e6220" /> 
<br/>
Một số thống kê cơ bản về giá trị trung bình, phân phối chuẩn, tứ phân vị hay các giá trị duy nhất, tấn suất xuất hiện bao nhiêu
<img width="718" height="462" alt="Screenshot 2025-07-11 214928" src="https://github.com/user-attachments/assets/f1c78f90-4a30-4804-a0c7-4a9a7d9a5158" />

# Data Processing
Dữ liệu trước khi đưa vào huấn luyện được xử lý về chuẩn hóa (Normalization), chuyển từ dạng category về các giá trị số tương ứng bằng phương pháp tương ứng (Ordinal hay One hot encoding), thực hiện xử lý cân bằng biến mục tiêu hoặc thêm một số cột mới để việc đào tạo mô hình được hiệu quả <br/>
Thực hiện xử lý cân bằng biến mục tiêu
<img width="1021" height="422" alt="Screenshot 2025-07-08 185816" src="https://github.com/user-attachments/assets/36d04214-a9ae-4955-80a0-4a95621e9b72" />
Bộ dữ liệu sau khi được xử lý
<img width="553" height="603" alt="Screenshot 2025-07-09 074558" src="https://github.com/user-attachments/assets/8a324f67-1118-45cc-b2f8-639e75c96af0" />

# Train & Evaluate
Để mô hình học tập hiệu quả các tham số truyền vào cần được xác định phù hợp. Phương pháp tìm kiếm các tham số được sử dụng thử trong một phạm vi nhất định và đánh giá qua các chỉ số như độ chuẩn xác, độ nhạy, độ chính xác, ma trận nhầm lẫn,... từ đó đưa ra tham số tối ưu. <br/>
Mô hình với số lớp là 15 và tiêu chí xác định bằng gini index được đánh giá tối ưu cho bài toán
<img width="915" height="422" alt="Screenshot 2025-07-09 083137" src="https://github.com/user-attachments/assets/7624221a-e493-4304-a696-ed03e369060d" />
<br/>
Trực quan hóa mô hình <br/>
Yếu tố tác động lớn nhất tới quyết định khách hàng có được phê duyệt hay không là duration (thời lượng liên hệ cuối cùng)
[tree_map.pdf](https://github.com/user-attachments/files/21201911/tree_map.pdf)

