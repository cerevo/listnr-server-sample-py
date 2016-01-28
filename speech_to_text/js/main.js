function getDateStr(date) {
    var month = date.getMonth() + 1;
    var day = date.getDate();
    var hour = ('00' + date.getHours()).substr(-2);
    var min = ('00' + date.getMinutes()).substr(-2);
    var sec = ('00' + date.getSeconds()).substr(-2);
    return month + '/' + day + ' ' + hour + ':' + min + ':' + sec;
}

document.addEventListener("DOMContentLoaded", function () {
    Array.prototype.forEach.call(document.querySelectorAll('.time'), function (elem) {
        var date = new Date(elem.dataset.time * 1000);
        elem.textContent = getDateStr(date);
    });
});
