
function displayBase64() {

  console.log(this.files[0])
  if (this.files && this.files[0]) {

    var FR= new FileReader();
    FR.readAsDataURL(this.files[0]);
    FR.onload = function () {
      console.log(FR.result);
      document.getElementById("phpfile").value = FR.result;
   };
   FR.onerror = function (error) {
     console.log('Error: ', error);
   };
  }
}
document.getElementById("zip").addEventListener("change", displayBase64);
