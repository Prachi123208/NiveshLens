EXPLANATIONS = {
    "Guaranteed Return": {
        "why": "The message suggests that a financial outcome is guaranteed, fixed, or risk-free.",
        "action": "Do not rely on the promise alone. Verify the claim independently before taking action."
    },
    "Urgency Pressure": {
        "why": "The message tries to create pressure by suggesting that you must act immediately.",
        "action": "Pause. Take time to verify the information instead of making a decision under pressure."
    },
    "Authority Claim": {
        "why": "The message uses a regulator, government body, or official-sounding name to appear trustworthy.",
        "action": "Verify the specific claim through the relevant official source independently."
    },
    "Payment Request": {
        "why": "The message asks you to send money or make a payment.",
        "action": "Verify the recipient and purpose of the payment independently before sending money."
    },
    "Secretive Language": {
        "why": "The message discourages you from discussing the opportunity with other people.",
        "action": "Do not allow secrecy pressure to stop you from checking the information independently."
    },
    "Credential Request": {
        "why": "The message appears to request sensitive credentials or authentication information.",
        "action": "Never share passwords, PINs, or authentication codes through an unverified request."
    },
    "Suspicious Link": {
        "why": "The message contains a link or asks you to click something that may lead to an unverified destination.",
        "action": "Avoid suspicious links and navigate to the relevant official website independently."
    },
    "Fake Reward": {
        "why": "The message claims that you have won a prize, reward, or cash benefit.",
        "action": "Verify the reward independently and do not provide sensitive information or payment just to claim it."
    }
}


HINDI_EXPLANATIONS = {
    "Guaranteed Return": {
        "why": "यह संदेश किसी वित्तीय लाभ को गारंटीड, निश्चित या बिना जोखिम वाला बताता है।",
        "action": "केवल इस वादे पर भरोसा न करें। कोई भी कदम उठाने से पहले दावे को स्वतंत्र रूप से सत्यापित करें।"
    },
    "Urgency Pressure": {
        "why": "यह संदेश आपको तुरंत निर्णय लेने के लिए दबाव डाल रहा है।",
        "action": "रुकें और समय लेकर जानकारी की स्वतंत्र रूप से जाँच करें।"
    },
    "Authority Claim": {
        "why": "यह संदेश भरोसा पैदा करने के लिए किसी रेगुलेटर, सरकारी संस्था या आधिकारिक नाम का उपयोग करता है।",
        "action": "दावे को संबंधित आधिकारिक स्रोत से स्वतंत्र रूप से सत्यापित करें।"
    },
    "Payment Request": {
        "why": "यह संदेश आपसे पैसे भेजने या भुगतान करने के लिए कह रहा है।",
        "action": "पैसे भेजने से पहले प्राप्तकर्ता और भुगतान के उद्देश्य को स्वतंत्र रूप से सत्यापित करें।"
    },
    "Secretive Language": {
        "why": "यह संदेश आपको इस अवसर के बारे में दूसरों से बात न करने के लिए कहता है।",
        "action": "गोपनीयता के दबाव में आकर जानकारी की जाँच करना बंद न करें।"
    },
    "Credential Request": {
        "why": "यह संदेश संवेदनशील अकाउंट या authentication जानकारी माँगता हुआ दिखाई देता है।",
        "action": "अनजान या सत्यापित न किए गए अनुरोध पर पासवर्ड, PIN या OTP साझा न करें।"
    },
    "Suspicious Link": {
        "why": "यह संदेश किसी लिंक पर क्लिक करने या किसी अनजान वेबसाइट पर जाने के लिए कहता है।",
        "action": "संदिग्ध लिंक से बचें और संबंधित आधिकारिक वेबसाइट को स्वयं खोलकर जानकारी सत्यापित करें।"
    },
    "Fake Reward": {
        "why": "यह संदेश दावा करता है कि आपने कोई इनाम, पुरस्कार या नकद राशि जीती है।",
        "action": "इनाम को स्वतंत्र रूप से सत्यापित करें और केवल इनाम पाने के लिए संवेदनशील जानकारी या पैसे साझा न करें।"
    }
}


HINDI_SIGNAL_NAMES = {
    "Guaranteed Return": "गारंटीड रिटर्न",
    "Urgency Pressure": "तुरंत कार्रवाई का दबाव",
    "Authority Claim": "अथॉरिटी / आधिकारिक दावा",
    "Payment Request": "भुगतान का अनुरोध",
    "Secretive Language": "गोपनीयता का दबाव",
    "Credential Request": "संवेदनशील जानकारी का अनुरोध",
    "Suspicious Link": "संदिग्ध लिंक",
    "Fake Reward": "फर्जी इनाम / पुरस्कार"
}


# =========================================================
# VERIFICATION PATH
# =========================================================

VERIFICATION_PATHS = {

    "Guaranteed Return": {
        "en": [
            "Treat guaranteed or risk-free return claims as a reason to pause.",
            "Check the claim through an independent and trusted source.",
            "Do not treat a promise of profit as proof that the opportunity is genuine."
        ],
        "hi": [
            "गारंटीड या बिना जोखिम वाले रिटर्न के दावे पर तुरंत भरोसा न करें।",
            "दावे को किसी स्वतंत्र और भरोसेमंद स्रोत से जाँचें।",
            "सिर्फ मुनाफे के वादे को अवसर के असली होने का प्रमाण न मानें।"
        ]
    },

    "Urgency Pressure": {
        "en": [
            "Pause instead of acting because of the deadline or urgency.",
            "Verify the information independently before taking any action.",
            "Do not let pressure make you skip basic verification."
        ],
        "hi": [
            "डेडलाइन या जल्दबाजी के कारण तुरंत कार्रवाई न करें।",
            "कोई भी कदम उठाने से पहले जानकारी को स्वतंत्र रूप से सत्यापित करें।",
            "दबाव के कारण जानकारी की जाँच करना न छोड़ें।"
        ]
    },

    "Authority Claim": {
        "en": [
            "Do not trust the regulatory or government name only because it appears in the message.",
            "Check the specific claim through the relevant organization's official source.",
            "Use the official website or independently verified contact information, not the message link."
        ],
        "hi": [
            "सिर्फ किसी सरकारी या रेगुलेटरी नाम के इस्तेमाल से संदेश पर भरोसा न करें।",
            "दावे को संबंधित संस्था के आधिकारिक स्रोत से जाँचें।",
            "मैसेज में दिए लिंक के बजाय आधिकारिक वेबसाइट या स्वतंत्र रूप से सत्यापित संपर्क जानकारी का उपयोग करें।"
        ]
    },

    "Payment Request": {
        "en": [
            "Identify who is requesting the payment and why.",
            "Verify the recipient and purpose independently.",
            "Do not send money only because the message creates urgency or pressure."
        ],
        "hi": [
            "पहचानें कि भुगतान कौन माँग रहा है और किस उद्देश्य से।",
            "प्राप्तकर्ता और भुगतान के उद्देश्य को स्वतंत्र रूप से सत्यापित करें।",
            "सिर्फ मैसेज के दबाव में आकर पैसे ट्रांसफर न करें।"
        ]
    },

    "Secretive Language": {
        "en": [
            "Treat requests to keep an opportunity secret as a warning signal.",
            "Take time to verify the information independently.",
            "If needed, discuss the claim with a trusted person before acting."
        ],
        "hi": [
            "किसी अवसर को गुप्त रखने के अनुरोध को चेतावनी संकेत मानें।",
            "जानकारी को स्वतंत्र रूप से जाँचने के लिए समय लें।",
            "जरूरत होने पर कार्रवाई से पहले किसी भरोसेमंद व्यक्ति से चर्चा करें।"
        ]
    },

    "Credential Request": {
        "en": [
            "Do not share OTPs, passwords, PINs, or authentication codes.",
            "Verify the request through the organization's official channel.",
            "Never use an unverified message as the reason to disclose sensitive credentials."
        ],
        "hi": [
            "OTP, पासवर्ड, PIN या authentication code साझा न करें।",
            "अनुरोध को संबंधित संस्था के आधिकारिक माध्यम से सत्यापित करें।",
            "सिर्फ किसी अनजान या सत्यापित न किए गए मैसेज के आधार पर संवेदनशील जानकारी साझा न करें।"
        ]
    },

    "Suspicious Link": {
        "en": [
            "Avoid clicking links from suspicious or unexpected messages.",
            "Open the relevant official website independently instead.",
            "Compare the information there with the claim made in the message."
        ],
        "hi": [
            "संदिग्ध या अनजान मैसेज में दिए लिंक पर क्लिक करने से बचें।",
            "इसके बजाय संबंधित आधिकारिक वेबसाइट को स्वयं खोलें।",
            "वहाँ उपलब्ध जानकारी की तुलना मैसेज के दावे से करें।"
        ]
    },

    "Fake Reward": {
        "en": [
            "Verify whether the prize or reward actually exists.",
            "Check the claim through an independent official source.",
            "Do not provide sensitive information or payment just to claim an unexpected reward."
        ],
        "hi": [
            "जाँचें कि बताया गया इनाम या पुरस्कार वास्तव में मौजूद है या नहीं।",
            "दावे को किसी स्वतंत्र आधिकारिक स्रोत से सत्यापित करें।",
            "अनजान इनाम को पाने के लिए संवेदनशील जानकारी या पैसे साझा न करें।"
        ]
    }
}