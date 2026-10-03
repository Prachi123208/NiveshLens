import re


RISK_PATTERNS = {

    "Guaranteed Return": [
        r"\bguaranteed\b",
        r"\bguarantee[d]?\b",
        r"\bfixed return\b",
        r"\b100% profit\b",
        r"\brisk[- ]free\b",
        r"\bno loss\b",
        r"\bguaranteed profit\b",

        "गारंटीड",
        "गारंटी",
        "पक्का मुनाफा",
        "बिना नुकसान"
    ],

    "Urgency Pressure": [
        r"\bonly today\b",
        r"\blimited time\b",
        r"\bact now\b",
        r"\blast chance\b",
        r"\bonly \d+ hours?\b",
        r"\bimmediately\b",

        "सिर्फ आज",
        "अभी करें",
        "तुरंत",
        "आखिरी मौका"
    ],

    "Authority Claim": [
        r"\bSEBI approved\b",
        r"\bRBI approved\b",
        r"\bgovernment approved\b",
        r"\bofficial scheme\b",
        r"\bgovernment scheme\b",

        "SEBI से मंजूर",
        "RBI से मंजूर",
        "सरकार द्वारा मंजूर",
        "सरकारी योजना"
    ],

    "Payment Request": [
        r"\bsend ₹?\s*\d+",
        r"\bpay ₹?\s*\d+",
        r"\btransfer ₹?\s*\d+",
        r"\bdeposit ₹?\s*\d+",
        r"\bpay us\b",

        r"₹\s*\d+.*भेजें",
        "पैसे भेजें",
        "भुगतान करें",
        "रकम जमा करें"
    ],

    "Secretive Language": [
        r"\bdon't tell anyone\b",
        r"\bdont tell anyone\b",
        r"\bkeep this secret\b",
        r"\bprivate opportunity\b",
        r"\bconfidential opportunity\b",

        "किसी को मत बताना",
        "गुप्त रखें",
        "किसी से साझा न करें"
    ],

    "Credential Request": [
        r"\bOTP\b",
        r"\bpassword\b",
        r"\bPIN\b",
        r"\baccount details\b",
        r"\blogin details\b",

        "ओटीपी",
        "पासवर्ड",
        "पिन",
        "खाते की जानकारी",
        "लॉगिन जानकारी"
    ]
}


# Different signals have different importance
RISK_WEIGHTS = {
    "Guaranteed Return": 20,
    "Urgency Pressure": 10,
    "Authority Claim": 15,
    "Payment Request": 20,
    "Secretive Language": 10,
    "Credential Request": 25
}


def detect_signals(text):

    detected = []

    text_lower = text.lower()

    for category, patterns in RISK_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, text_lower):

                detected.append(category)

                break

    return detected


def calculate_risk_score(signals):

    score = 0

    for signal in signals:

        score += RISK_WEIGHTS.get(signal, 0)

    if score > 100:
        score = 100

    return score