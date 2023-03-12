$(document).ready(function (){
    // add to cart
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
            complete: function () {
                location.reload()
            }
        })
    })

    //delete item from cart
    $(".btn-delete").on('click', function () {
        var _pId = $(this).attr('data-item')
        $.ajax({
            type: "POST",
            url: "/delete-from-cart",
            data: {
                'id': _pId,
            },
            dataType: "json",
            complete: function () {
                location.reload()
            }
        })
    })

    //reduce quantity item
    $(".reduceFromCartBtn").on('click', function () {
        var _vm=$(this);
        var _qty = $("#quantity").val()
        if (!_qty)
            _qty = 1
        var _productId = $(this).attr("data-id")
        var _productTitle = $(this).attr("data-title")
        var _productPrice = $(this).attr("data-price")
        var _productImage = $(this).attr("data-image")
        $.post({
            url: "/reduce-from-cart",
            data: {
                'id': _productId,
                'name': _productTitle,
                'price': _productPrice,
                'image': _productImage,
                'quantity': _qty
            },
            dataType: 'json',
            complete: function () {
                location.reload()
            }
        })
    })
})

