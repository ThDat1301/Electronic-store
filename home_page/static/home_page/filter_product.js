$(document).ready(function() {
    $(".filter-checkbox, #btnFilterPrice").on('click', function() {
        var filterArr = {};
        var minPrice = $("#maxPrice").attr('min');
        var maxPrice = $("#maxPrice").val();
        filterArr.minPrice = minPrice;
        filterArr.maxPrice = maxPrice;

        $.ajax({
            url:'/filter_product',
            data: filterArr,
            dataType:"json",
            beforeSend: function() {
                $("#productList").html("<div>Loading</div>");
            },
            success: function(res){
                $("#productList").html(res.data);
            }
         });

    });

});