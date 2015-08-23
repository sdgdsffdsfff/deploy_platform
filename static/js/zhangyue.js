$(document).ready(function(){
  $("#view_save").click(function(){
        if($("#pro_name").val()=="" || $("#git_addr").val()==""){
                alert("项目名称或git地址不能为空");
            }else{
                $.post("/post_view/",
                {
                        pro_name:   	$("#pro_name").val(),
                        pro_desc:   	$("#pro_desc").val(),
                        git_addr:   	$("#git_addr").val(),
                        exec_shell_1:  	$("#exec_shell_1").val(),
                        exec_shell_2:  	$("#exec_shell_2").val(),
                        ssh_server:   	$("#ssh_server option:selected").text(),
                        local_path:   	$("#local_path").val(),
                        remove_path:  	$("#remove_path").val(),
                        remote_path:   	$("#remote_path").val(),
                        mail_name:   	$("#mail_name").val(),
                        mail_subject:  	$("#mail_subject").val(),
                        mail_data:   	$("#mail_data").val(),
                    remote_exec_shell: 	$("#remote_exec_shell").val(),
                },
                        function(data){
                                	alert(data);
                });
                                location.href='/';
        };
  });

///////////////////////////////////////////////////////////////


  $("#Group_btn").click(function(){
        if($("#Group_Name").val()==""){
                alert("组名字不能为空");
            }else{
                $.post("/add_group/",
                {
                        Group_Name:       $("#Group_Name").val(),
                        Group_Desc:       $("#Group_Desc").val(),
                },
                        function(data){
                                        alert(data);
                });
                                location.href='/';
        };
  });

////////////////////////////////////////////////////////////
  $("#myTab li :not(li:last)").click(function(){
	alert("wqdqdqwd");
  });

});
