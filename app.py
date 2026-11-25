from flask import Flask, request

app = Flask(__name__)
app.config.update(
    MAX_CONTENT_LENGTH=16 * 1024,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Strict",
    SESSION_COOKIE_SECURE=True,
)


@app.after_request
def apply_security_headers(response):
    response.headers["Content-Security-Policy"] = (
        "default-src 'none'; frame-ancestors 'none'; base-uri 'none'; "
        "form-action 'none'"
    )
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    response.headers["Cross-Origin-Resource-Policy"] = "same-origin"
    response.headers["Permissions-Policy"] = (
        "accelerometer=(), autoplay=(), camera=(), display-capture=(), "
        "encrypted-media=(), fullscreen=(), geolocation=(), gyroscope=(), "
        "magnetometer=(), microphone=(), midi=(), payment=(), "
        "picture-in-picture=(), publickey-credentials-get=(), "
        "screen-wake-lock=(), sync-xhr=(), usb=(), web-share=(), "
        "xr-spatial-tracking=()"
    )
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Permitted-Cross-Domain-Policies"] = "none"
    proto = request.headers.get("X-Forwarded-Proto", request.scheme)
    if proto.split(",", 1)[0].strip().lower() == "https":
        response.headers["Strict-Transport-Security"] = (
            "max-age=31536000; includeSubDomains"
        )
    return response


@app.route("/")
def home():
    return "Hello from OpenCode!", 200, {"Content-Type": "text/plain; charset=utf-8"}


@app.route("/health")
def health():
    return "OK", 200, {"Content-Type": "text/plain; charset=utf-8"}
