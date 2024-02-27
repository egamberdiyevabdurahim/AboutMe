let hr = document.querySelector("#hrs");
let mn = document.querySelector("#min");
let sc = document.querySelector("#sec");

setInterval(() => {
  let day = new Date();

let hh = day.getHours() * 30;
let mm = day.getMinutes() * 6;
let ss =day.getSeconds() * 6;

hr.style.transform = `rotateZ(${hh+(mm/12)}deg)`;
mn.style.transform = `rotateZ(${mm}deg)`;
sc.style.transform = `rotateZ(${ss}deg)`;

// time square

let hour = document.querySelector("#hour");
let minutes = document.querySelector("#minutes");
let seconds = document.querySelector("#seconds");
let ampm = document.querySelector("#ampm");

let h = new Date().getHours();
let m = new Date().getMinutes();
let s = new Date().getSeconds();

let am = h >= 12 ?"PM" : "AM";

if(h > 12)[
  h = h -12
]

hour.innerHTML = h < 10 ? "0" + h : h ;
minutes.innerHTML = m  < 10 ? "0" + m : m ;
seconds.innerHTML = s  < 10 ? "0" + s : s ;

ampm.innerHTML = am

},);