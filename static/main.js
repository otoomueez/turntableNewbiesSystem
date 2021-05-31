
//var fullHeight = function() {
//
//	('.js-fullheight').css('height', (window).height());
//	(window).resize(function(){
//		('.js-fullheight').css('height', (window).height());
//	});
//
//};
//fullHeight();


document.querySelector('#sidebarCollapse').addEventListener('click', function () {
    console.log(document.querySelector('#sidebar').style.margin == '0px 0px 0px -250px')
    if (document.querySelector('#sidebar').style.margin == '0px 0px 0px -250px'){
        document.querySelector('#sidebar').style.margin = '0px'
        }
    else{
        document.querySelector('#sidebar').style.margin = '0px 0px 0px -250px'}
    console.log('Button pressed')
    console.log(document.querySelector('#sidebar').classList)
});




