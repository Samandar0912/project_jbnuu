var mainSwiper = new Swiper(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 20,
    loop: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
});

var mainSwiper = new Swiper(".mySwiper1", {
    slidesPerView: 3,
    spaceBetween: 50,
    loop: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
});

var sustemSwiper = new Swiper(".sysSwiper", {
    slidesPerView: 4,
    spaceBetween: 10,
    loop: true,
    navigation: {
        nextEl: ".systemRight",
        prevEl: ".systemLeft",
    },
    breakpoints: {
        320: {
            slidesPerView: 1,
            spaceBetween: 20
        },
        480: {
            slidesPerView: 1,
            spaceBetween: 30
        },
        640: {
            slidesPerView: 2,
            spaceBetween: 20
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 30
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 30
        },
        1440: {
            slidesPerView: 4,
            spaceBetween: 30
        }
    }
});
var siteSwiper = new Swiper(".sitSwiper", {
    slidesPerView: 4,
    spaceBetween: 50,
    loop: true,
    navigation: {
        nextEl: ".sitRight",
        prevEl: ".sitLeft",
    },
    breakpoints: {
        320: {
            slidesPerView: 1,
            spaceBetween: 20
        },
        480: {
            slidesPerView: 1,
            spaceBetween: 30
        },
        640: {
            slidesPerView: 2,
            spaceBetween: 20
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 30
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 30
        },
        1440: {
            slidesPerView: 4,
            spaceBetween: 30
        }
    }
});