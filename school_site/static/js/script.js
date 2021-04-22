$("[data-scroll]").on('click', function (event) {
    event.preventDefault();

    let elemID = $(this).data('scroll');
    let elemOffSet = $(elemID).offset().top;

    $('html, body').animate({
        scrollTop: elemOffSet
    });
});