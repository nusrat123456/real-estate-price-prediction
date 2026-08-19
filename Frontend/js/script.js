const API="http://127.0.0.1:8000";

const form=document.getElementById("predictionForm");
const result=document.getElementById("result");
const historyBody=document.getElementById("historyBody");
const btn=document.getElementById("predictBtn");

loadHistory();

form.addEventListener("submit",async(e)=>{

e.preventDefault();

const area=Number(document.getElementById("area").value);
const bedrooms=Number(document.getElementById("bedrooms").value);
const bathrooms=Number(document.getElementById("bathrooms").value);
const location=document.getElementById("location").value.trim();

if(area<=0||bedrooms<=0||bathrooms<=0){
alert("Please enter valid values.");
return;
}

btn.disabled=true;
btn.innerHTML="Predicting...";

try{

const response=await fetch(`${API}/predictions/predict/`,{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
area,
bedrooms,
bathrooms,
location
})
});

const data=await response.json();

if(response.ok){

result.style.transform="scale(.8)";
result.style.opacity="0";

setTimeout(()=>{
    result.innerHTML=`₹ ${Number(data.predicted_price).toLocaleString("en-IN",{maximumFractionDigits:2})}`;
    result.style.transform="scale(1)";
    result.style.opacity="1";
},250);

setTimeout(()=>{
result.innerHTML=`₹ ${Number(data.predicted_price).toLocaleString("en-IN",{maximumFractionDigits:2})}`;
result.style.opacity="1";
},200);

form.reset();

loadHistory();

}else{

alert(data.error||"Prediction failed.");

}

}catch(err){

console.error(err);
alert("Backend server is not running.");

}

btn.disabled=false;
btn.innerHTML="✨ Predict Price";

});

async function loadHistory(){

try{

const response=await fetch(`${API}/predictions/history/`);
const data=await response.json();

historyBody.innerHTML="";

data.slice().reverse().slice(0,5).forEach(item=>{

historyBody.innerHTML+=`
<tr>
<td>${item.location}</td>
<td>${item.area}</td>
<td>₹ ${Number(item.predicted_price).toLocaleString("en-IN",{maximumFractionDigits:2})}</td>
</tr>
`;

});

}catch(e){

console.log(e);

}

}