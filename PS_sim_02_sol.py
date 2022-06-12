import random


def make_random_sentence(adverbs, actions, adjectives, nouns):
    adverb = random.choice(adverbs)
    action = random.choice(actions)
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return (f'{adverb} {action} {adjective} {noun}')


def main():
    adverbs = ["phosfluorescently", "authoritatively", "enthusiastically", "monotonectally", "appropriately"]
    actions = ["strategize", "unleash", "right-shore", "expedite", "enhance", "initiate", "evisculate", "matrix", "communicate", "simplify", "predominate", "supply", "facilitate", "exploit", "re-engineer", "visualize", "syndicate", "repurpose", "transition", "architect", "grow", "e-enable", "develop", "evolve", "redefine"]
    adjectives = ["cross functional", "standardized", "state of the art", "sticky", "seamless", "team driven", "cutting-edge", "world-class", "resource-sucking", "cross-media", "holistic", "accurate", "compelling", "resource-maximizing", "high standards in", "top-line", "timely", "viral", "interdependent", "robust", "prospective"]
    nouns = ["innovation", "action items", "data", "technology", "testing procedures", "e-services", "materials", "benefits", "vortals"]
    print(make_random_sentence(adverbs, actions, adjectives, nouns))


