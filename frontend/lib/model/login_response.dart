
class LoginResponse {
  final bool success;
  final String auth_token;

  LoginResponse({required this.success});

  factory LoginResponse.fromJson(Map<String, dynamic> json) {
    return LoginResponse(
      success: json['success'],
      authToken: json['auth_token'],
    );
  }
}