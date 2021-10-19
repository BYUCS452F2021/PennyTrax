
class InstitutionLinkResponse {
  final String linkURL;

  InstitutionLinkResponse({required this.linkURL});

  factory InstitutionLinkResponse.fromJson(Map<String, dynamic> json) {
    return InstitutionLinkResponse(
      linkURL: json['link_url'],
    );
  }
}