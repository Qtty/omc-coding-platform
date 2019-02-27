var button=document.getElementById('btn');


console.log(button)
button.addEventListener("click",function(){
  var formulaire=document.getElementById('register');
  var formData=new FormData(formulaire);
      var ourRequest= new XMLHttpRequest();
      ourRequest.open('POST','/process');
        ourRequest.onload=function(){
        console.log(ourRequest.responseText);

          //console.log(formulaire);
    }
ourRequest.send(formData);})