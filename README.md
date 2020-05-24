# School-schedule

GIẢI PHÁP
	-Biến: 
	  .Các ca học (1,2,3,4) của thứ (2,3,4,5,6,7). Tổng cộng ta có 24 biến.
	  .Các thứ sẽ là tập của các biến.
	-Miền giá trị: 
	  .Các buổi học của môn.
	  .Mỗi buổi học sẽ có 2 giá trị: Tên môn học và lớp yêu cầu.
	  Ràng buộc: Ca học có phòng yêu cầu nếu không thì phải có phòng thay thế gần với phòng yêu cầu.
	-Hàm lợi ích: 
	  .Giảm thiểu thời gian đi và về. 
	  .Giảm thiểu khoảng cách đi lại giữa các phòng học.
	-Thuật toán: 
	  .Ta sẽ sắp xếp lịch học sao cho đảm bảo thỏa mãn ràng buộc đồng thời giảm thiểu thời gian đi và về.
	  .Giảm thiểu khoảng cách giữa các lớp học bằng cách tìm các giá trị có phòng yêu cầu gần với phòng yêu cầu ở ca trước đó bằng thuật 		toán Beam search.
	  .Khi phòng yêu cầu không có ta sẽ tìm các phòng thay thế gần với phòng yêu cầu bằng thuật toán Beam seach.
