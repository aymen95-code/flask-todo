const checkBtn = document.querySelectorAll('.check');
//const tbRow = checkBtn.parentNode.parentNode;

console.log(checkBtn)

for(let i=0; i < checkBtn.length; i++) {
    checkBtn[i].addEventListener('click', (e) => {
        let trow = checkBtn[i].parentNode.parentNode;
        trow.classList.toggle('checked')
    });
};
