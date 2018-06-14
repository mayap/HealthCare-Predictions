const url = window.location.href;

$(document).ready(function(){
    $('.classifier-result-text').css('visibility', 'hidden');
    $('.classifier-result-text').text('');
});

const predictButton = $('.predict-button');
const classifierImageWrapper = $('.classifier-image-wrapper');
const classifierFormTextarea = $('.classifier-form textarea');
const validateLabel = $('.validate-label');
const classifierResultText = $('.classifier-result-text');
const classifierImageLink = $('.classifier-image-link');
classifierImageLink.attr("href", url + 'tree');

function makePrediction() {
    predictButton.addClass('loading');
    predictButton.text('Loading...');
    classifierImageWrapper.css('display', 'none');
    classifierResultText.css('visibility', 'hidden');
    classifierResultText.text('');

    var data = classifierFormTextarea.val();

    if (!data) {
        validateLabel.text('Please make sure that you entered data!');
        validateLabel.addClass('validate-label-error');
        classifierFormTextarea.addClass('validate-textarea-error');

        predictButton.removeClass('loading');
        predictButton.text('Predict');

        return;
    } else {
        validateLabel.text('');
        validateLabel.removeClass('validate-label-error');
        classifierFormTextarea.removeClass('validate-textarea-error');
    }

    data = data.split(',');

    var newData = data.map(function(el) {
        return el.trim();
    });

    if (newData.length != 12) {
        validateLabel.text('Please make sure that you entered 12 integer or float numbers!');
        validateLabel.addClass('validate-label-error');
        classifierFormTextarea.addClass('validate-textarea-error');

        predictButton.removeClass('loading');
        predictButton.text('Predict');

        return;
    } else {
        validateLabel.text('');
        validateLabel.removeClass('validate-label-error');
        classifierFormTextarea.removeClass('validate-textarea-error');
    }

    $.ajax({
        type: "POST",
        url: url + 'prediction',
        data: JSON.stringify(newData),
        headers: {
            "content-type": "application/json"
        },
        success: success
    });
}

function success(result) {
    result = JSON.parse(result);

    classifierFormTextarea.val('');
    classifierResultText.css('visibility', 'visible');
    classifierResultText.text(result.prediction);

    classifierImageWrapper.css('display', 'block');

    predictButton.removeClass('loading');
    predictButton.text('Predict');
}
