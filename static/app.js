const arrows = document.querySelectorAll(".arrow");
const booklists = document.querySelectorAll(".book-list");

arrows.forEach((arrow,i)=>{
    
    const itemNumber=booklists[i].querySelectorAll("img").length;
    let clickCounter =0;
    arrow.addEventListener("click",()=>{
        const ratio = Math.floor(window.innerWidth/270);
        clickCounter++;
        if(itemNumber - (3 + clickCounter) + (4-ratio) >= 0){
        booklists[i].style.transform = `translateX(${booklists[i].computedStyleMap().get("transform")[0].x.value-300}px)`;
    } else {
        booklists[i].style.transform = "translateX(0)";
        clickCounter = 0;
    }
    });

    
    //console.log(booklists[i].querySelectorAll("img").length)
    //console.log(Math.floor(window.innerWidth/270));
});


//toggle
const ball = document.querySelector(".toggle-ball");
const items = document.querySelectorAll(".container,.book-list-title,.navbar-container,.sidebar,.left-menu-icon,.toggle");

ball.addEventListener("click",()=>{
    items.forEach(item=>{
        item.classList.toggle("active")
    })
    ball.classList.toggle("active")
})

