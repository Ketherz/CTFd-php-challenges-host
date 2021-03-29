CTFd._internal.challenge.data = undefined

CTFd._internal.challenge.renderer = CTFd.lib.markdown();


CTFd._internal.challenge.preRender = function() {}

CTFd._internal.challenge.render = function(markdown) {

    return CTFd._internal.challenge.renderer.render(markdown)
}


CTFd._internal.challenge.postRender = function() {}


CTFd._internal.challenge.submit = function(preview) {
    var challenge_id = parseInt(CTFd.lib.$('#challenge-id').val())
    var submission = CTFd.lib.$('#challenge-input').val()

    var body = {
        'challenge_id': challenge_id,
        'submission': submission,
    }
    var params = {}
    if (preview) {
        params['preview'] = true
    }

    return CTFd.api.post_challenge_attempt(params, body).then(function(response) {
        if (response.status === 429) {
            // User was ratelimited but process response
            return response
        }
        if (response.status === 403) {
            // User is not logged in or CTF is paused.
            return response
        }
        return response
    })
};



var modal =
    '<div class="modal fade" tabindex="-1" role="dialog">' +
    '  <div class="modal-dialog" role="document">' +
    '    <div class="modal-content">' +
    '      <div class="modal-header">' +
    '        <h5 class="modal-title">{0}</h5>' +
    '        <button type="button" class="close" data-dismiss="modal" aria-label="Close">' +
    '          <span aria-hidden="true">&times;</span>' +
    "        </button>" +
    "      </div>" +
    '      <div class="modal-body">' +
    "        <p>{1}</p>" +
    "      </div>" +
    '      <div class="modal-footer">' +
    "      </div>" +
    "    </div>" +
    "  </div>" +
    "</div>";

function ezal(args) {
    var res = modal.format(args.title, args.body);
    var obj = $(res);
    var button = '<button type="button" class="btn btn-primary" data-dismiss="modal">{0}</button>'.format(
        args.button
    );
    obj.find(".modal-footer").append(button);
    $("main").append(obj);

    obj.modal("show");

    $(obj).on("hidden.bs.modal", function(e) {
        $(this).modal("dispose");
    });

    return obj;
}
