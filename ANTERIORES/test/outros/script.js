
openMenu.addEventListener('click', () => {
    menu.style.display = 'flex'
    
    setTimeout(() => {
    menu.style.opacity = '1'    
    }, 10);
})

clodeMenu.addEventListener('click', () => {
    menu.style.opacity = '0'
    
    setTimeout(() => {
    menu.removeAttribute('style')    
    }, 200);
    
})