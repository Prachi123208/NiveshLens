import re


# =========================================================
# RISK PATTERNS
# =========================================================

RISK_PATTERNS = {

    "Guaranteed Return": [
        r"\bguaranteed\b",
        r"\bguarantee[d]?\b",
        r"\bguaranteed return\b",
        r"\bfixed return\b",
        r"\b100% profit\b",
        r"\brisk[- ]free\b",
        r"\bno loss\b",
        r"\bguaranteed profit\b",
        r"\b40% return\b",
        r"\b\d+%\s*guaranteed\b",
        "गारंटीड",
        "गारंटी",
        "पक्का मुनाफा",
        "बिना नुकसान",
        "गारंटीड रिटर्न"
    ],

    "Urgency Pressure": [
        r"\bonly today\b",
        r"\blimited time\b",
        r"\bact now\b",
        r"\blast chance\b",
        r"\bonly \d+ hours?\b",
        r"\bwithin \d+ hours?\b",
        r"\bimmediately\b",
        r"\bhurry\b",
        r"\bdeadline\b",
        "सिर्फ आज",
        "अभी करें",
        "तुरंत",
        "आखिरी मौका",
        "जल्दी करें"
    ],

    "Authority Claim": [
        r"\bSEBI approved\b",
        r"\bRBI approved\b",
        r"\bgovernment approved\b",
        r"\bofficial scheme\b",
        r"\bgovernment scheme\b",
        r"\bSEBI registered\b",
        r"\bRBI registered\b",
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
        r"\bsend money\b",
        r"\btransfer money\b",
        r"₹\s*\d+.*भेजें",
        "पैसे भेजें",
        "भुगतान करें",
        "रकम जमा करें",
        "पैसे ट्रांसफर करें"
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
        r"\bverification code\b",
        r"\bsecurity code\b",
        "ओटीपी",
        "पासवर्ड",
        "पिन",
        "खाते की जानकारी",
        "लॉगिन जानकारी"
    ],

    "Suspicious Link": [
        r"https?://",
        r"www\.",
        r"\bclick here\b",
        r"\bclick the link\b",
        r"\bverify your account\b",
        r"\bopen this link\b",
        "लिंक पर क्लिक",
        "यहाँ क्लिक करें"
    ],

    "Fake Reward": [
        r"\byou have won\b",
        r"\byou won\b",
        r"\bcongratulations\b.*\bprize\b",
        r"\bclaim your reward\b",
        r"\bclaim prize\b",
        r"\blucky winner\b",
        r"\bcash prize\b",
        r"\bfree reward\b",
        "आप जीत गए",
        "इनाम जीतें",
        "पुरस्कार",
        "बधाई हो",
        "रिवॉर्ड प्राप्त करें"
    ]
}


# =========================================================
# RISK WEIGHTS
# =========================================================

RISK_WEIGHTS = {
    "Guaranteed Return": 20,
    "Urgency Pressure": 10,
    "Authority Claim": 15,
    "Payment Request": 20,
    "Secretive Language": 10,
    "Credential Request": 25,
    "Suspicious Link": 15,
    "Fake Reward": 15
}


# =========================================================
# CLAIM BREAKDOWN
# =========================================================

CLAIM_BREAKDOWN = {

    "Guaranteed Return": {
        "claim": "The message suggests a guaranteed, fixed, or risk-free financial outcome.",
        "pattern": "Guaranteed or risk-free return language",
        "verify": "Check whether the claim is supported by reliable and independent information."
    },

    "Urgency Pressure": {
        "claim": "The message creates pressure to act immediately.",
        "pattern": "Time pressure or limited-time language",
        "verify": "Pause and verify the information independently before acting."
    },

    "Authority Claim": {
        "claim": "The message uses a regulator, government body, or official-sounding name to create trust.",
        "pattern": "Authority or regulatory reference",
        "verify": "Verify the specific claim through the relevant official source rather than the message link."
    },

    "Payment Request": {
        "claim": "The message asks the recipient to send money or make a payment.",
        "pattern": "Direct payment or money-transfer request",
        "verify": "Verify the recipient, purpose, and payment request independently before sending money."
    },

    "Secretive Language": {
        "claim": "The message discourages the recipient from discussing the opportunity with others.",
        "pattern": "Secrecy or confidentiality pressure",
        "verify": "Do not let secrecy pressure prevent you from independently checking the information."
    },

    "Credential Request": {
        "claim": "The message requests sensitive account or authentication information.",
        "pattern": "OTP, PIN, password, or account-detail request",
        "verify": "Never share passwords, PINs, or authentication codes through an unverified request."
    },

    "Suspicious Link": {
        "claim": "The message directs the recipient to a link or asks them to click something.",
        "pattern": "External link or click-to-verify language",
        "verify": "Avoid using links from suspicious messages and navigate to the relevant official website independently."
    },

    "Fake Reward": {
        "claim": "The message claims that the recipient has won a prize, reward, or cash benefit.",
        "pattern": "Unexpected reward or prize claim",
        "verify": "Verify that the reward is genuine through an independent and trusted source before providing information or payment."
    }
}


# =========================================================
# DETECT RISK SIGNALS
# =========================================================

def detect_signals(text):

    detected = []

    if not text:
        return detected

    for category, patterns in RISK_PATTERNS.items():

        for pattern in patterns:

            # IGNORECASE fixes matching issues such as
            # "OTP", "otp", "SEBI Approved", etc.
            if re.search(pattern, text, re.IGNORECASE):

                detected.append(category)
                break

    return detected


# =========================================================
# CALCULATE RISK SCORE
# =========================================================

def calculate_risk_score(signals):

    score = 0

    for signal in signals:
        score += RISK_WEIGHTS.get(signal, 0)

    # Keep score between 0 and 100
    score = min(score, 100)

    return score


# =========================================================
# GET CLAIM BREAKDOWN
# =========================================================

def get_claim_breakdown(signals):

    breakdown = []

    for signal in signals:

        if signal in CLAIM_BREAKDOWN:

            breakdown.append({
                "signal": signal,
                "claim": CLAIM_BREAKDOWN[signal]["claim"],
                "pattern": CLAIM_BREAKDOWN[signal]["pattern"],
                "verify": CLAIM_BREAKDOWN[signal]["verify"]
            })

    return breakdown