/* Javascript for H5pXBlock. */
function H5pXBlock(runtime, element) {

    function updateCount(result) {
        $('.count', element).text(result.result);
    }
    var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    var checklist = [];
    var score = 0;
    var attempts = 0;
    var numCard = $('.block-memory-card').length / 2;

    $('.block-memory-card').click(function(event,eventObject) {
        $(event.target).parent('div').addClass('block-flipped');
        var id = $(event.target).parent('div').attr("id");

        checklist.push(id);

        if (checklist.length > 1) {

            if (checklist[0] == checklist[1]) {

                $.ajax({
                    type: "POST",
                    url: handlerUrl,
                    data: JSON.stringify({
                        "result": "success"
                    }),
                    success: updateCount
                });

                $this = $('.block-memory-card.block-flipped');
                $this.addClass('block-matched');
                $this.addClass('block-flippedM');
                $this.removeClass("block-flipped");

                checklist = [];
                score += 1;
                attempts += 1;

                if (score == numCard) {
                    alert("You Win!");
                }
            } else if (checklist[0] != checklist[1]) {
                setTimeout(function() {
                    $('.block-memory-card.block-flipped').removeClass("block-flipped");
                }, 1000);
                checklist = [];
                attempts += 1;
            } else {
                checklist = [];
            }
        }
    });

    $(function($) {
        /* Here's where you'd do things on page load. */
    });
}
