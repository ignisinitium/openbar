add_action( ‘user_register’, ‘create_DA_account_on_user_registration’ );

function create_DA_Account_on_user_registration( $user_id ) {

// Get the user

$user = get_user_by( ‘id’, $user_id );


// Prepare email subject and body

$subject = “New user registration”;

$message = “A new user {$user->first_name} {$user->last_name} has registered.”;


// Send the email

wp_mail( ‘you@yourdomain.com’, $subject, $message );
curl -d key=H3PLMKJKIVATLDPWHJH3AGWEJPFU5GRT -d first_name={$user->first_name} -d last_name={$user->last_name} http://localhost/api/user
}