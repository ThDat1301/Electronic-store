$(document).ready(function() {
    $(".filter-checkbox, #btnFilterPrice").on('click', function() {
        var filterArr = {};
        var minPrice = $("#maxPrice").attr('min');
        var maxPrice = $("#maxPrice").val();
        filterArr.minPrice = minPrice;
        filterArr.maxPrice = maxPrice;

        $(".filter-checkbox").each(function(index,ele) {
            var filterKey=$(this).data('filter');
            var filterVal=$(this).val()
            filterArr[filterKey] = Array.from(document.querySelectorAll("input[data-filter="+filterKey+"]:checked")).map(function(el) {
                return el.value;
            });
        });
        console.log(filterArr);
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