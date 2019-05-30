$(function(){
	  $("#file").change(function(){  // 当 id 为 file 的对象发生变化时
	    var fileSize = this.files[0].size;
	    var size = fileSize / 1024 / 1024;
	    if (size > 50) {
	        alert("附件不能大于50M,请将文件压缩后重新上传！");
	        this.value="";
	        return false;
	    }else{
	        $("#file_name").text($("#file").val());  //将 #file 的值赋给 #file_name
			$("#file_name").val($("#file").val());
	    }
	});

	var p = $(".node1.col-md-3")
	var details = $(".details")
	p.click(function(){

		var index = p.index($(this));
		console.log(p)
		details.removeClass('active');
		details.eq(index).addClass("active");
		});
});