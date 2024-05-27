// JS-шаблон создания новой карточки приема к мастеру

$('#id_date').on('blur', function(event) {
    var date = event.target.value,
        master_id = $('#id_master').val();

    if(date && master_id){
        getFreeTimeChoices(master_id, date)
    }
});


$('#id_mast').on('change', function(event) {
    var maste_id = event.target.value,
        date = $('#id_date').val();

    if(date &&master_id){
        getFreeTimeChoices(master_id, date)
    }
});


// Отправляет запрос за свободным рабочим времене мастера в конкретный день
function getFreeTimeChoices(maste_id, date) {
    $.get(
        "/reception/get-free-time-choices",
        {
            doctor_id: doctor_id,
            date: date
        },
        setFreeTimeChoices
    );

    // Заполняет поле выбора времени приема свободными значениями времени мастера
    function setFreeTimeChoices(data) {

        $(data.free_time).each(function (i) {
            var value = data.free_time[i][0],
                text = data.free_time[i][1];
            $("#id_time").append($('<option></option>').val(value).html(text));
        });
    }
}