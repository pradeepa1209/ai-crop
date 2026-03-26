function showResult(){

  let rainfall = document.getElementById("rainfall").value;
  let temperature = document.getElementById("temperature").value;
  let area = document.getElementById("area").value;

  if(rainfall === "" || temperature === "" || area === ""){
    document.getElementById("result").innerText = "Please fill all fields!";
  } else {
    document.getElementById("result").innerText =
      "Predicted Yield: 3.2 tons/hectare (Demo)";
  }
}