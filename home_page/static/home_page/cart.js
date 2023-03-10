$(document).ready(function (){
    $(".addToCartBtn").on('click', function () {
        var _vm=$(this);
        var _qty = $("#quantity").val()
        if (!_qty)
            _qty = 1
        var _productId = $(this).attr("data-id")
        var _productTitle = $(this).attr("data-title")
        var _productPrice = $(this).attr("data-price")
        var _productImage = $(this).attr("data-image")
        $.post({
            url: "/add-to-cart",
            data: {
                'id': _productId,
                'name': _productTitle,
                'price': _productPrice,
                'image': _productImage,
                'quantity': _qty
            },
            dataType: 'json',
            beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				$(".cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
			}
        })
    })
})