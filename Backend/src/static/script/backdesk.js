$(document).ready(function () {

    // 啟動 tooltips 功能
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    });

    // editModal 事件
    $('#editModal').on('shown.bs.modal', function (event) {

        // 取得「觸發 Modal 的按鈕」
        var btn = $(event.relatedTarget);

        // 取出「按鈕的 data-title 值」
        var title = btn.data('title');

        var user = btn.data('user');
        var email = btn.data('email');
        var item = btn.data('item');
        var quantity = btn.data('quantity');
        var order = btn.data('order');

        // modal = 它自己 = 開啟的 Modal 本身
        var modal = $(this);

        modal.find('.modal-title').text(title);
        modal.find('#userName').val(user);
        modal.find('#userEmail').val(email);
        modal.find('#itemName').attr('placeholder', item);
        modal.find('#itemQuantity').val(quantity);

        console.log(order);

        // 設定「品項的 input」的「disabled」狀態
        // if 「是“快速下單”按鈕」
        if (order === 'fast') {
            // 「品項的 input」就「不會是 disabled」
            modal.find('#itemName').attr('disabled', false);
        } else {
            modal.find('#itemName').attr('disabled', true);
        }

    });

    // removeModal 事件
    $('#removeModal').on('shown.bs.modal', function (event) {

        var btn = $(event.relatedTarget);

        var title = btn.data('title');

        var modal = $(this);

        modal.find('.modal-title').text('刪除 ' + title);

    });



});



