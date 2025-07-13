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
Trực quan hóa mô hình 
[Uploading decistio|--- feature_7 <= -0.49
|   |--- feature_19 <= 1.49
|   |   |--- feature_0 <= 2.37
|   |   |   |--- feature_9 <= 2.90
|   |   |   |   |--- feature_0 <= -1.86
|   |   |   |   |   |--- class: 1
|   |   |   |   |--- feature_0 >  -1.86
|   |   |   |   |   |--- feature_7 <= -0.89
|   |   |   |   |   |   |--- feature_9 <= 2.72
|   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |--- feature_9 >  2.72
|   |   |   |   |   |   |   |--- feature_16 <= 0.67
|   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |--- feature_16 >  0.67
|   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |--- feature_7 >  -0.89
|   |   |   |   |   |   |--- feature_16 <= 0.67
|   |   |   |   |   |   |   |--- feature_8 <= -0.39
|   |   |   |   |   |   |   |   |--- feature_4 <= 0.22
|   |   |   |   |   |   |   |   |   |--- feature_9 <= 0.45
|   |   |   |   |   |   |   |   |   |   |--- feature_9 <= 0.15
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_9 >  0.15
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 3
|   |   |   |   |   |   |   |   |   |--- feature_9 >  0.45
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_4 >  0.22
|   |   |   |   |   |   |   |   |   |--- feature_4 <= 0.76
|   |   |   |   |   |   |   |   |   |   |--- feature_0 <= 1.13
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_0 >  1.13
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_4 >  0.76
|   |   |   |   |   |   |   |   |   |   |--- feature_7 <= -0.50
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |   |--- feature_7 >  -0.50
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |--- feature_8 >  -0.39
|   |   |   |   |   |   |   |   |--- feature_12 <= -0.19
|   |   |   |   |   |   |   |   |   |--- feature_4 <= -0.47
|   |   |   |   |   |   |   |   |   |   |--- feature_7 <= -0.68
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_7 >  -0.68
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_4 >  -0.47
|   |   |   |   |   |   |   |   |   |   |--- feature_17 <= 1.21
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 4
|   |   |   |   |   |   |   |   |   |   |--- feature_17 >  1.21
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 2
|   |   |   |   |   |   |   |   |--- feature_12 >  -0.19
|   |   |   |   |   |   |   |   |   |--- feature_7 <= -0.88
|   |   |   |   |   |   |   |   |   |   |--- feature_21 <= 0.55
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |   |--- feature_21 >  0.55
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 2
|   |   |   |   |   |   |   |   |   |--- feature_7 >  -0.88
|   |   |   |   |   |   |   |   |   |   |--- feature_2 <= 0.50
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 3
|   |   |   |   |   |   |   |   |   |   |--- feature_2 >  0.50
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |--- feature_16 >  0.67
|   |   |   |   |   |   |   |--- feature_4 <= -0.54
|   |   |   |   |   |   |   |   |--- feature_4 <= -0.54
|   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_4 >  -0.54
|   |   |   |   |   |   |   |   |   |--- feature_7 <= -0.67
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_7 >  -0.67
|   |   |   |   |   |   |   |   |   |   |--- feature_7 <= -0.65
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |   |   |--- feature_7 >  -0.65
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |--- feature_4 >  -0.54
|   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |--- feature_9 >  2.90
|   |   |   |   |--- feature_0 <= 1.04
|   |   |   |   |   |--- class: 0
|   |   |   |   |--- feature_0 >  1.04
|   |   |   |   |   |--- class: 1
|   |   |--- feature_0 >  2.37
|   |   |   |--- feature_4 <= -0.47
|   |   |   |   |--- class: 0
|   |   |   |--- feature_4 >  -0.47
|   |   |   |   |--- feature_20 <= -0.56
|   |   |   |   |   |--- class: 0
|   |   |   |   |--- feature_20 >  -0.56
|   |   |   |   |   |--- feature_7 <= -0.86
|   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |--- feature_7 >  -0.86
|   |   |   |   |   |   |--- feature_4 <= 1.21
|   |   |   |   |   |   |   |--- feature_8 <= -0.39
|   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |--- feature_8 >  -0.39
|   |   |   |   |   |   |   |   |--- feature_0 <= 2.79
|   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |--- feature_0 >  2.79
|   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |--- feature_4 >  1.21
|   |   |   |   |   |   |   |--- class: 0
|   |--- feature_19 >  1.49
|   |   |--- feature_7 <= -0.87
|   |   |   |--- class: 0
|   |   |--- feature_7 >  -0.87
|   |   |   |--- feature_4 <= 1.51
|   |   |   |   |--- feature_9 <= 1.51
|   |   |   |   |   |--- feature_7 <= -0.52
|   |   |   |   |   |   |--- feature_2 <= 0.50
|   |   |   |   |   |   |   |--- feature_8 <= -0.39
|   |   |   |   |   |   |   |   |--- feature_7 <= -0.71
|   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_7 >  -0.71
|   |   |   |   |   |   |   |   |   |--- feature_0 <= -0.87
|   |   |   |   |   |   |   |   |   |   |--- feature_12 <= -0.19
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |   |   |--- feature_12 >  -0.19
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_0 >  -0.87
|   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |--- feature_8 >  -0.39
|   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |--- feature_2 >  0.50
|   |   |   |   |   |   |   |--- feature_7 <= -0.56
|   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |--- feature_7 >  -0.56
|   |   |   |   |   |   |   |   |--- feature_4 <= 0.23
|   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_4 >  0.23
|   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |--- feature_7 >  -0.52
|   |   |   |   |   |   |--- class: 0
|   |   |   |   |--- feature_9 >  1.51
|   |   |   |   |   |--- class: 0
|   |   |   |--- feature_4 >  1.51
|   |   |   |   |--- class: 0
|--- feature_7 >  -0.49
|   |--- feature_7 <= 0.80
|   |   |--- feature_16 <= 0.67
|   |   |   |--- feature_19 <= 1.49
|   |   |   |   |--- feature_21 <= -1.53
|   |   |   |   |   |--- feature_10 <= 0.93
|   |   |   |   |   |   |--- feature_18 <= 1.93
|   |   |   |   |   |   |   |--- feature_7 <= 0.39
|   |   |   |   |   |   |   |   |--- feature_4 <= 7.97
|   |   |   |   |   |   |   |   |   |--- feature_9 <= 1.18
|   |   |   |   |   |   |   |   |   |   |--- feature_13 <= 0.48
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_13 >  0.48
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_9 >  1.18
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_4 >  7.97
|   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |--- feature_7 >  0.39
|   |   |   |   |   |   |   |   |--- feature_0 <= 2.87
|   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_0 >  2.87
|   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |--- feature_18 >  1.93
|   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |--- feature_10 >  0.93
|   |   |   |   |   |   |--- class: 0
|   |   |   |   |--- feature_21 >  -1.53
|   |   |   |   |   |--- feature_9 <= 2.87
|   |   |   |   |   |   |--- feature_7 <= -0.08
|   |   |   |   |   |   |   |--- feature_1 <= 0.74
|   |   |   |   |   |   |   |   |--- feature_5 <= 0.01
|   |   |   |   |   |   |   |   |   |--- feature_8 <= -0.39
|   |   |   |   |   |   |   |   |   |   |--- feature_7 <= -0.11
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_7 >  -0.11
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_8 >  -0.39
|   |   |   |   |   |   |   |   |   |   |--- feature_10 <= 2.56
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 4
|   |   |   |   |   |   |   |   |   |   |--- feature_10 >  2.56
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |--- feature_5 >  0.01
|   |   |   |   |   |   |   |   |   |--- feature_0 <= 0.79
|   |   |   |   |   |   |   |   |   |   |--- feature_8 <= 0.36
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 4
|   |   |   |   |   |   |   |   |   |   |--- feature_8 >  0.36
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |--- feature_0 >  0.79
|   |   |   |   |   |   |   |   |   |   |--- feature_0 <= 1.13
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 4
|   |   |   |   |   |   |   |   |   |   |--- feature_0 >  1.13
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |--- feature_1 >  0.74
|   |   |   |   |   |   |   |   |--- feature_6 <= 1.17
|   |   |   |   |   |   |   |   |   |--- feature_0 <= 0.96
|   |   |   |   |   |   |   |   |   |   |--- feature_4 <= -0.52
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_4 >  -0.52
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |--- feature_0 >  0.96
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_6 >  1.17
|   |   |   |   |   |   |   |   |   |--- feature_0 <= 0.46
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_0 >  0.46
|   |   |   |   |   |   |   |   |   |   |--- feature_21 <= -0.40
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |   |--- feature_21 >  -0.40
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |--- feature_7 >  -0.08
|   |   |   |   |   |   |   |--- feature_4 <= 1.50
|   |   |   |   |   |   |   |   |--- feature_4 <= 0.08
|   |   |   |   |   |   |   |   |   |--- feature_4 <= -0.61
|   |   |   |   |   |   |   |   |   |   |--- feature_17 <= 1.21
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_17 >  1.21
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_4 >  -0.61
|   |   |   |   |   |   |   |   |   |   |--- feature_7 <= -0.05
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_7 >  -0.05
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |--- feature_4 >  0.08
|   |   |   |   |   |   |   |   |   |--- feature_5 <= 0.01
|   |   |   |   |   |   |   |   |   |   |--- feature_0 <= 1.46
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_0 >  1.46
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_5 >  0.01
|   |   |   |   |   |   |   |   |   |   |--- feature_1 <= -0.06
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |   |--- feature_1 >  -0.06
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |--- feature_4 >  1.50
|   |   |   |   |   |   |   |   |--- feature_24 <= -0.98
|   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |--- feature_24 >  -0.98
|   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |--- feature_9 >  2.87
|   |   |   |   |   |   |--- feature_4 <= 1.49
|   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |--- feature_4 >  1.49
|   |   |   |   |   |   |   |--- class: 0
|   |   |   |--- feature_19 >  1.49
|   |   |   |   |--- feature_4 <= 3.60
|   |   |   |   |   |--- feature_10 <= 4.18
|   |   |   |   |   |   |--- feature_26 <= 7.66
|   |   |   |   |   |   |   |--- feature_9 <= 1.23
|   |   |   |   |   |   |   |   |--- feature_2 <= -0.78
|   |   |   |   |   |   |   |   |   |--- feature_21 <= -1.37
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_21 >  -1.37
|   |   |   |   |   |   |   |   |   |   |--- feature_10 <= 1.20
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |   |   |--- feature_10 >  1.20
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_2 >  -0.78
|   |   |   |   |   |   |   |   |   |--- feature_0 <= 2.33
|   |   |   |   |   |   |   |   |   |   |--- feature_10 <= 0.93
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 4
|   |   |   |   |   |   |   |   |   |   |--- feature_10 >  0.93
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |   |--- feature_0 >  2.33
|   |   |   |   |   |   |   |   |   |   |--- feature_14 <= -0.44
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |   |   |--- feature_14 >  -0.44
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |--- feature_9 >  1.23
|   |   |   |   |   |   |   |   |--- feature_7 <= -0.29
|   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_7 >  -0.29
|   |   |   |   |   |   |   |   |   |--- feature_8 <= 0.55
|   |   |   |   |   |   |   |   |   |   |--- feature_2 <= -2.05
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 2
|   |   |   |   |   |   |   |   |   |   |--- feature_2 >  -2.05
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |   |--- feature_8 >  0.55
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |--- feature_26 >  7.66
|   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |--- feature_10 >  4.18
|   |   |   |   |   |   |--- class: 0
|   |   |   |   |--- feature_4 >  3.60
|   |   |   |   |   |--- class: 0
|   |   |--- feature_16 >  0.67
|   |   |   |--- feature_7 <= 0.20
|   |   |   |   |--- feature_0 <= -1.53
|   |   |   |   |   |--- feature_1 <= -0.55
|   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |--- feature_1 >  -0.55
|   |   |   |   |   |   |--- class: 0
|   |   |   |   |--- feature_0 >  -1.53
|   |   |   |   |   |--- feature_4 <= 0.79
|   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |--- feature_4 >  0.79
|   |   |   |   |   |   |--- feature_4 <= 0.81
|   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |--- feature_4 >  0.81
|   |   |   |   |   |   |   |--- class: 0
|   |   |   |--- feature_7 >  0.20
|   |   |   |   |--- feature_7 <= 0.60
|   |   |   |   |   |--- feature_0 <= -0.04
|   |   |   |   |   |   |--- feature_6 <= 1.17
|   |   |   |   |   |   |   |--- feature_11 <= 1.15
|   |   |   |   |   |   |   |   |--- feature_8 <= 0.36
|   |   |   |   |   |   |   |   |   |--- feature_4 <= -0.31
|   |   |   |   |   |   |   |   |   |   |--- feature_4 <= -0.46
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_4 >  -0.46
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_4 >  -0.31
|   |   |   |   |   |   |   |   |   |   |--- feature_4 <= 1.16
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 3
|   |   |   |   |   |   |   |   |   |   |--- feature_4 >  1.16
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_8 >  0.36
|   |   |   |   |   |   |   |   |   |--- feature_0 <= -0.20
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_0 >  -0.20
|   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |--- feature_11 >  1.15
|   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |--- feature_6 >  1.17
|   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |--- feature_0 >  -0.04
|   |   |   |   |   |   |--- class: 0
|   |   |   |   |--- feature_7 >  0.60
|   |   |   |   |   |--- feature_11 <= 1.15
|   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |--- feature_11 >  1.15
|   |   |   |   |   |   |--- feature_2 <= 0.50
|   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |--- feature_2 >  0.50
|   |   |   |   |   |   |   |--- class: 1
|   |--- feature_7 >  0.80
|   |   |--- feature_12 <= -0.19
|   |   |   |--- feature_0 <= 1.04
|   |   |   |   |--- feature_10 <= 3.10
|   |   |   |   |   |--- feature_9 <= 0.80
|   |   |   |   |   |   |--- feature_9 <= 0.64
|   |   |   |   |   |   |   |--- feature_10 <= 1.47
|   |   |   |   |   |   |   |   |--- feature_6 <= 1.17
|   |   |   |   |   |   |   |   |   |--- feature_7 <= 0.98
|   |   |   |   |   |   |   |   |   |   |--- feature_7 <= 0.93
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 3
|   |   |   |   |   |   |   |   |   |   |--- feature_7 >  0.93
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_7 >  0.98
|   |   |   |   |   |   |   |   |   |   |--- feature_4 <= 2.46
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_4 >  2.46
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_6 >  1.17
|   |   |   |   |   |   |   |   |   |--- feature_1 <= -0.06
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_1 >  -0.06
|   |   |   |   |   |   |   |   |   |   |--- feature_4 <= -0.56
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |   |--- feature_4 >  -0.56
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |--- feature_10 >  1.47
|   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |--- feature_9 >  0.64
|   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |--- feature_9 >  0.80
|   |   |   |   |   |   |--- class: 1
|   |   |   |   |--- feature_10 >  3.10
|   |   |   |   |   |--- class: 0
|   |   |   |--- feature_0 >  1.04
|   |   |   |   |--- feature_16 <= 0.67
|   |   |   |   |   |--- class: 0
|   |   |   |   |--- feature_16 >  0.67
|   |   |   |   |   |--- feature_1 <= -1.20
|   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |--- feature_1 >  -1.20
|   |   |   |   |   |   |--- class: 1
|   |   |--- feature_12 >  -0.19
|   |   |   |--- feature_4 <= -0.72
|   |   |   |   |--- class: 0
|   |   |   |--- feature_4 >  -0.72
|   |   |   |   |--- feature_14 <= -0.44
|   |   |   |   |   |--- feature_7 <= 1.14
|   |   |   |   |   |   |--- feature_0 <= 0.17
|   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |--- feature_0 >  0.17
|   |   |   |   |   |   |   |--- feature_6 <= 1.17
|   |   |   |   |   |   |   |   |--- feature_10 <= 5.80
|   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_10 >  5.80
|   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |--- feature_6 >  1.17
|   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |--- feature_7 >  1.14
|   |   |   |   |   |   |--- feature_4 <= 0.75
|   |   |   |   |   |   |   |--- feature_1 <= -0.06
|   |   |   |   |   |   |   |   |--- feature_20 <= -0.56
|   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_20 >  -0.56
|   |   |   |   |   |   |   |   |   |--- feature_2 <= -2.05
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_2 >  -2.05
|   |   |   |   |   |   |   |   |   |   |--- feature_0 <= -0.41
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 2
|   |   |   |   |   |   |   |   |   |   |--- feature_0 >  -0.41
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |--- feature_1 >  -0.06
|   |   |   |   |   |   |   |   |--- feature_8 <= 0.36
|   |   |   |   |   |   |   |   |   |--- feature_4 <= -0.45
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_4 >  -0.45
|   |   |   |   |   |   |   |   |   |   |--- feature_0 <= 0.42
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_0 >  0.42
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |--- feature_8 >  0.36
|   |   |   |   |   |   |   |   |   |--- feature_5 <= 0.01
|   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_5 >  0.01
|   |   |   |   |   |   |   |   |   |   |--- feature_6 <= 1.17
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |   |   |--- feature_6 >  1.17
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 2
|   |   |   |   |   |   |--- feature_4 >  0.75
|   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |--- feature_14 >  -0.44
|   |   |   |   |   |--- feature_9 <= 2.70
|   |   |   |   |   |   |--- feature_4 <= 3.28
|   |   |   |   |   |   |   |--- feature_0 <= -1.53
|   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |--- feature_0 >  -1.53
|   |   |   |   |   |   |   |   |--- feature_7 <= 5.79
|   |   |   |   |   |   |   |   |   |--- feature_10 <= 0.39
|   |   |   |   |   |   |   |   |   |   |--- feature_17 <= 1.21
|   |   |   |   |   |   |   |   |   |   |   |--- truncated branch of depth 5
|   |   |   |   |   |   |   |   |   |   |--- feature_17 >  1.21
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |--- feature_10 >  0.39
|   |   |   |   |   |   |   |   |   |   |--- feature_4 <= -0.52
|   |   |   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |   |   |   |   |--- feature_4 >  -0.52
|   |   |   |   |   |   |   |   |   |   |   |--- class: 1
|   |   |   |   |   |   |   |   |--- feature_7 >  5.79
|   |   |   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |   |--- feature_4 >  3.28
|   |   |   |   |   |   |   |--- class: 0
|   |   |   |   |   |--- feature_9 >  2.70
|   |   |   |   |   |   |--- class: 0
n_tree.log…]()

[tree_map.pdf](https://github.com/user-attachments/files/21201911/tree_map.pdf)

