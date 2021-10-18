class RegisterRequest {
  final String first_name;
  final String last_name;
  final String email;
  final String password;
  final String salt;

  RegisterRequest({
    @required this.first_name,
    @required this.last_name,
    @required this.email,
    @required this.password,
    @required this.salt,
  });

  factory RegisterRequest.fromJson(Map<String, dynamic> json) {
    return RegisterRequest(
      first_name: json['first_name'] as string,
      last_name: json['last_name'] as string,
      email: json['email'] as string,
      password: json['password'] as string,
      salt: json['salt'] as string,
    );
  }
}