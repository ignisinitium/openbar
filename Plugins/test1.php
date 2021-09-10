// http://51.81.84.150/api/user/new

$server = http://51.81.84.150/api/
$apicall = $server + $api[i]

$apicalls (
"user/new" ,
"user_list
","user_info
","user
","user
","user/<user_id>
","user/<user_id>
","user/<user_id>
","fields
","privileges
","privileges
","user/<user_id>/privileges
","user/<user_id>/privileges
","interviews
","interviews
","user/interviews
","user/interviews
","user/<user_id>/interviews
","user/<user_id>/interviews
","list
","secret
","login_url
","resume_url
","temp_url
","session/new
","session/question
","session/action
","session/back
","session
","file/<file_number>
","playground
","playground
","playground
","playground_install
","playground/project
","playground/project
","playground/project
","clear_cache
","config
","config
","package
","package
","package_update_status
","user/api
","user/api
","user/api
","user/api
","user/<user_id>/api
","user/<user_id>/api
","user/<user_id>/api
","user/<user_id>/api
","convert_file
","interview_data
","stash_data" ,
"retrieve_stashed_data"
)

function wp_remote_get( $url, $args = array() ) {
    $http = _wp_http_get_object();
    return $http->get( $url, $args );
}