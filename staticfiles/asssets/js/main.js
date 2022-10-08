//search
const navbarSearch = document.querySelector('.navbar--list__search a')
const navbarSearchForm = document.querySelector('.navbar--form')
navbarSearch.addEventListener('click', function(){
	if(navbarSearchForm.classList.contains('active')){
		navbarSearchForm.classList.remove('active')
	}else{
		navbarSearchForm.classList.add('active')

	}
})
//list menu
const navbarButton = document.querySelector('.navbar__menu-button')
const navbarPages = document.querySelector('.navbar--list__pages')
const navbarExit = document.querySelector('.exit')
navbarButton.addEventListener('click', function(){
	navbarPages.classList.add('active')
	
})
navbarExit.addEventListener('click', function(){
	navbarPages.classList.remove('active')
	
})
//slider

var splide = new Splide( '.splide', {
	type   : 'loop',
  } );
  
  splide.mount();

class SLIDER{
	constructor(obj){
	  this.slider = obj.slider
	  this.sliderList = this.slider.querySelector('.slider-list')
	  this.sliderItem = this.slider.querySelectorAll('.slider-list__item')
	  this.prev = this.slider.querySelector('.prevv')
	  this.next = this.slider.querySelector('.nextt')
	  this.activeSlide = 0
	  this.timeMove = 1000
	  this.moveSlide = 100
	  this.dir = obj.direction
	  this.isSwipe = false,

	  this.interval = obj.interval
	  this.play = obj.autoplay
	  this.dots = obj.createDots
	  
	  this.sliderItem.forEach((slide, key)=>{
		if(key != this.activeSlide){
		  slide.style.transform = `translate${this.dir}(${this.moveSlide}%)` 
		}
		if(key == this.sliderItem.length-1){
		  slide.style.transform = `translate${this.dir}(${-this.moveSlide}%)`     
		}
	  })
	  // dots
	  if(this.dots == true){
		const ul = document.createElement('ul')
		ul.classList.add('slider-dots')
		this.sliderItem.forEach(()=>{
		  const li = document.createElement('li')
		  ul.append(li)
		})
		this.slider.append(ul)
		this.sliderDots = this.slider.querySelectorAll('.slider-dots li')
		this.sliderDots[this.activeSlide].classList.add('active')
		
		this.sliderDots.forEach((dot, key)=>{
		  dot.addEventListener('click', ()=>{
			this.controllers(key)
		  })
		})      
		this.active = true
	  }
	  // autoplay
	  if(this.play == true){
		let autoplay = setInterval(() => {
		  this.move(this.next)
		}, this.interval);
		this.slider.addEventListener('mouseenter', ()=>{
		  clearInterval(autoplay)
		})
		this.slider.addEventListener('mouseleave', ()=>{
		  autoplay = setInterval(() => {
			this.move(this.next)
		  }, this.interval);
		})  
	  }
	  this.prev.addEventListener('click', ()=>{this.move(this.prev)})
	  this.next.addEventListener('click', ()=>{this.move(this.next)})
  
	}
	move(btn){
	  this.next.disabled = true
	  this.prev.disabled = true
	  setTimeout(() => {
	  this.next.disabled = false
	  this.prev.disabled = false
	  }, this.timeMove+200);
	  let btnPrexorNext = btn == this.next ? -this.moveSlide: this.moveSlide
	  this.sliderItem.forEach((slide, key)=>{
	  if(key != this.activeSlide){
		slide.style.transform = `translate${this.dir}(${-btnPrexorNext}%)` 
		slide.style.transition = `0ms` 
	  }
	  })
	  setTimeout(() => {
	  this.sliderItem[this.activeSlide].style.transform = `translate${this.dir}(${btnPrexorNext}%)` 
	  this.sliderItem[this.activeSlide].style.transition = `${this.timeMove}ms`     
	  if(this.dots == true){this.sliderDots[this.activeSlide].classList.remove('active')}
	  if(btn == this.next){
		this.activeSlide++
		if(this.activeSlide > this.sliderItem.length -1){
		  this.activeSlide = 0
		}
	  }else if (btn == this.prev){
		this.activeSlide--
		if(this.activeSlide < 0){
		  this.activeSlide = this.sliderItem.length -1
		}
	  }  
	  this.sliderItem[this.activeSlide].style.transform = `translate${this.dir}(0%)` 
	  this.sliderItem[this.activeSlide].style.transition = `${this.timeMove}ms` 
	  if(this.dots == true){this.sliderDots[this.activeSlide].classList.add('active')}
	  }, 200);
	}
	controllers(dotkey){
	  if(this.active && dotkey != this.activeSlide){    
		this.sliderItem.forEach((skude)=>{
		  skude.style.transition = '0ms'
		})
		this.active = false
		this.next.disabled = true
		this.prev.disabled = true
		this.sliderDots.forEach((dot)=>{dot.classList.remove('active')})
		let moveLeftOrRight = dotkey > this.activeSlide ? -this.moveSlide : this.moveSlide
		this.sliderItem[dotkey].style.transform = `translate${this.dir}(${-this.moveLeftOrRight}%)`
		setTimeout(() => {
		  this.sliderItem[this.activeSlide].style.transform = `translate${this.dir}(${moveLeftOrRight}%)`
		  this.sliderItem[this.activeSlide].style.transition = `${this.timeMove}ms`
		  this.sliderDots[this.activeSlide].classList.remove('active')
		  this.activeSlide = dotkey
		  this.sliderItem[this.activeSlide].style.transform = `translate${this.dir}(0%)`
		  this.sliderItem[this.activeSlide].style.transition = `${this.timeMove}ms`
		  this.sliderDots[this.activeSlide].classList.add('active')
	
		},);
		setTimeout(() => {
		  this.active = true
		  this.next.disabled = false
		  this.prev.disabled = false
		}, this.timeMove + 200);
	  }
	}
}
  const sliders = document.querySelectorAll('.slider')
  for(const slider of sliders){
	const autoplay = slider.hasAttribute('autoplay') ? true : false
	const dots = slider.hasAttribute('create-dots') ? true : false
	const interval = slider.getAttribute('interval') >= 2000 ? slider.getAttribute('interval') : 2000;
	const direction = slider.getAttribute('direction') == 'Y' || slider.getAttribute('direction')== 'y' ? 'Y' : 'X';
	new SLIDER({
	  slider: slider,
	  createDots: dots,
	  autoplay: autoplay,
	  interval: interval,
	  direction: direction,
	})
  }