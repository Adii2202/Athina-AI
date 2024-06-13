from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from rag.AIVoiceAssistant import AIVoiceAssistant

ai_assistant = AIVoiceAssistant()

def evaluate_assistant(assistant, test_queries, expected_answers):
    predicted_answers = []
    for query in test_queries:
        predicted_answer = assistant.interact_with_llm(query)
        predicted_answers.append(predicted_answer)

    # Calculate accuracy
    accuracy = accuracy_score(expected_answers, predicted_answers)

    # If answers are available for evaluation, calculate precision, recall, and F1-score
    if expected_answers:
        precision = precision_score(expected_answers, predicted_answers, average='micro')
        recall = recall_score(expected_answers, predicted_answers, average='micro')
        f1 = f1_score(expected_answers, predicted_answers, average='micro')
        print("Precision: {:.2f}".format(precision))
        print("Recall: {:.2f}".format(recall))
        print("F1 Score: {:.2f}".format(f1))

    print("Accuracy: {:.2f}".format(accuracy))

# Test queries and expected answers (ground truth)
test_queries = [
    "What is the definition of 'vandalism' in the Churchill insurance policy?",
    "How can I contact Churchill for windscreen claims?",
    "Does Churchill provide coverage for modifications made to a car by a previous owner?",
    "What is the purpose of DriveSure in Churchill insurance?",
    "Can I use my car abroad with Churchill insurance?",
    "How can I obtain a Braille, large print, or audio version of my insurance documents from Churchill?",
    "What is the difference between commuting and business use in Churchill insurance?",
    "Are electric car charging cables covered under Churchill insurance?",
    "How does Churchill determine premiums for DriveSure policyholders?",
    "What is the contact email for DriveSure help with Churchill insurance?",
    "Does Churchill offer coverage for damage caused by automated car functions?",
    "What is the territorial coverage provided by Churchill insurance?",
    "How can I make a claim with Churchill insurance?",
    "Are electric car batteries covered under Churchill insurance?",
    "What does the term 'Partner' refer to in the Churchill insurance policy?",
    "What is the purpose of the Green Card when traveling abroad with Churchill insurance?",
    "How does Churchill handle repairs for insured cars?",
    "What is the coverage for trailers under Churchill insurance?",
    "Can I get a European Accident Statement from Churchill?",
    "What is the purpose of the Glossary section in the Churchill insurance policy?",
    "How can I get a Braille version of my insurance documents from Churchill?",
    "What is the coverage for personal belongings under Churchill insurance?",
    "What is the purpose of the Motor Legal Cover helpline with Churchill insurance?",
    "How does Churchill handle claims for windscreen damage?",
    "What is the coverage for Guaranteed Hire Car Plus under Churchill insurance?",
    "Can I use my car for business purposes with Churchill insurance?",
    "What is the purpose of the FAQs section in the Churchill insurance policy?",
    "How does Churchill handle claims for accidental damage to cars?",
    "What is the coverage for liability to other people under Comprehensive Plus with Churchill insurance?",
    "How does Churchill handle losses caused by automated car functions?"
]

expected_answers = [
    "Vandalism in the Churchill insurance policy refers to damage caused by a malicious and deliberate act [T1].",
    "To make windscreen claims with Churchill, you can call 0800 328 9150 [T2].",
    "Yes, Churchill insurance covers modifications made to your car by a previous owner, including changes to appearance or performance [T1].",
    "DriveSure is Churchill's telematics insurance product designed to monitor how, when, and where your car is driven to adjust premiums based on driving behavior [T3].",
    "The ability to use your car abroad with Churchill insurance depends on your policy type and destination. Details can be found in the policy document [T3].",
    "To request a Braille, large print, or audio version of your documents from Churchill, you can call 0345 877 6680 [T2].",
    "Commuting in Churchill insurance refers to driving to and from a permanent place of work, while business use covers driving related to business or employment [T3].",
    "Electric car charging cables are considered accessories and are covered under 'Section 2: Fire and theft' or 'Section 4: Accidental damage' of the policy [T3].",
    "Churchill determines premiums for DriveSure policyholders based on driving behavior captured by the telematics technology [T3].",
    "For DriveSure help with Churchill insurance, you can email Support@churchill.com [T2].",
    "Churchill does not cover damage caused by automated car functions if their use is unlawful [T6].",
    "Churchill insurance provides coverage in Great Britain, Northern Ireland, the Channel Islands, and the Isle of Man [T1].",
    "To make a claim with Churchill insurance, you can call 0345 878 6261 [T2].",
    "Electric car batteries are covered if damaged as a result of an insured incident, whether owned or leased [T3].",
    "In the Churchill insurance policy, 'Partner' refers to your husband, wife, civil partner, or someone you're living with as if married [T1].",
    "The Green Card may be required when traveling abroad with Churchill insurance. It is recommended to contact Churchill before traveling to arrange for one [T3].",
    "Churchill customers have access to a national network of approved repairers who will manage all aspects of the repair process [T3].",
    "Churchill insurance covers trailers specially built to be towed by a car [T1].",
    "You can obtain a European Accident Statement from Churchill by visiting churchill.com/eas-form.pdf [T3].",
    "The Glossary section in the Churchill insurance policy provides definitions for specific terms used throughout the document [T4].",
    "To request a Braille version of your insurance documents from Churchill, you can call 0345 877 6680 [T2].",
    "Personal belongings may be covered under Section 6 of the policy, depending on the circumstances [T1].",
    "The Motor Legal Cover helpline with Churchill insurance is available for policyholders who have Motor Legal Cover and need assistance [T2].",
    "For windscreen claims with Churchill insurance, you can call 0800 328 9150 [T2].",
    "Churchill insurance offers Guaranteed Hire Car Plus coverage, as detailed in Section 8 of the policy [T4].",
    "Business use coverage in Churchill insurance allows for driving related to business or employment [T3].",
    "The FAQs section in the Churchill insurance policy provides answers to common questions policyholders may have [T4].",
    "Churchill insurance covers accidental damage to cars as outlined in Section 4 of the policy [T4].",
    "Comprehensive Plus coverage with Churchill insurance includes liability to other people within specified territorial limits for up to 90 days in every insured period [T5].",
    "Churchill does not cover losses, damages, or injuries caused by automated car functions if their use is unlawful [T6]."
]

# Evaluate the assistant
evaluate_assistant(ai_assistant, test_queries, expected_answers)
