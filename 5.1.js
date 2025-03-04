// Функция для подсчета частоты элементов в массиве
function countFrequency(arr) {
    return arr.reduce((acc, item) => {
        acc[item] = (acc[item] || 0) + 1
        return acc
    }, {})
}

// Исходный текст
const text = `Machiavelli revolutionized the way the worldviews politics. However, when we read his writings today, the ideas don’t seem very revolutionary. This is because his thoughts came to embody political structure. Machiavelli is known for being the first political philosopher to apply realism to politics. Machiavelli wanted to find a solution to his dark reality. Machiavelli’s The Prince presents us with the reality of the political arena, and provides us with the tools to work with human nature and its shortcomings. The Prince was written as a guide for Lorenzo de’Medici of Florence to stay in power. However, Lorenzo did not agree with Machiavelli’s assumptions. Machiavelli wants to restore pride and honor to Italy (Lerner, 1950). He offers a guide of how to accomplish this in the Prince. Machiavelli wrote the Prince when Europe was engulfed in civil wars. Machiavelli challenged the idea of divine right (Lerner, 1950). Machiavelli proposed the evolution of a new ruler, not chosen by divine right or heritage, but by military conquest. Previous to the publication of The Prince, Machiavelli had witnessed devastation in Italy (Lerner, 1950).
Machiavelli witnessed how power struggles and contradicting principles lead to the destruction of his nation. He wanted to offer a solution to his reality in The Prince. A nation wants stability, security, and prosperity. If the prince can provide all three while maintaining the common wealth of the people, then the ends justify the means. During the time at which Machiavelli wrote The Prince, these were revolutionary thoughts. Machiavelli’s writing was revolutionary for humanists in this era. He chose not analyze rule with divine foundations (Lerner, 1950). He rejected the notion of theology and divine right. Machiavelli decided to take a unique route. Machiavelli’s work is based on political realism. Machiavelli was the first to openly distinguish what we believe man to be, and who he really is. By acknowledging what human nature truly is, he was able to analyze the ways in which Princes can manipulate the people and their power to create a stable nation. This realism had never before been brought into political thinking.
Machiavelli argues that an ordinary citizen is the best person to analyze the ruling party. He argues that his bird’s eye view is the reason he is best suited for such analysis, “For the aim of the people is more honest than that of nobility, the latter desiring to oppress, and the former merely to avoid oppression” (Santoni, 112). Machiavelli acknowledges what Politics are rather then what then what we want them to be. Machiavelli does not say that politics can do everything and he does not say that politics can solve all societies problems. In The Prince, Machiavelli lays down the foundation for what a governor can do to maintain security, prosperity, and stability. Machiavelli does however, acknowledge that he cannot explain human nature, but rather the patterns that lie within it. Machiavelli acknowledges that he is an observer in The Prince. He uses an analogy of a man on a hill to explain the nature of his observation (Lerner, 1950). The man on the hill has the best view of the landscape. As a citizen he has observed the patterns in decision-making made by politicians and was able to interpret them.
Politics cannot answer all the questions in our society. Political thinking can only help to provide us with the framework with which we govern and are governed. The conflicting ethical principles are what cause the controversy. Machiavelli acknowledges this fact and shows that ethics are not what define politics, but are rather a component. Machiavelli argues that a Prince must be able to manipulate the attitudes of the people. Machiavelli speaks of the state. He speaks of national stability. He acknowledges that citizens and there beliefs are components of the state. The political realism emphasized in The Prince does not simply mean to accept ‘reason of the state’ as legitimacy and letting liberties be crushed (Lerner, 1950). The realism urges leaders to strive for coercion of principles. A leader unified under his people is most powerful.
In The Prince, Machiavelli offers a solution to the unsuccessful development of states. The Prince gains territory by victory and sets solid foundations for the territory to flourish upon, “One, however, who becomes Prince by favor of the populace, must maintain friendship, which he will find easy, the people asking nothing but not to be oppressed”(Santoni, 1950). Machiavelli believes that a good nation with just laws will develop from an efficient military. He is not arguing that you need a war to create a state, but rather a successful victory can create a solid foundation of the state. Machiavelli understands human nature and decides to work with it rather than disregard our flaws. He knows we are not all good, but acknowledges that there is potential for us to change (Lerner, 1950). Machiavelli does not argue that the goals of politicians are always good.
Machiavelli acknowledges that politicians ruthlessly seek power (Lerner, 1950). They do not care how it will affect the people. This is where a politician’s career crumbles. As noted in The Prince, you cannot rule a populace who hates you. They will overthrow you. Therefore, a prince must unite the people under his rule in order to obtain success. Human nature is the evil that is unconquerable. People will never stop having selfish motives. Therefore, we must learn to coordinate these desires. The Prince must give the people stability, security and prosperity. If he does this, then the people will dare not challenge him. Machiavelli does not provide us with an explanation of basic human nature but rather a framework, which we can use to govern and be governed.
Machiavelli wants to improve politics. In the Prince he offers a plan of how to govern and how the people should be governed. He accepts that human nature is flawed. He knows that rulers are power hungry (Lerner, 1950). He also acknowledges that a ruler will not have a populace to rule if the populace hates him. Machiavelli accepts what our politics is, and tells us of what it should be. Just because human nature is flawed, doesn’t mean we are hopeless. Humanity can achieve prosperity, security, and stability if achieved within the right framework. This framework is presented in The Prince. Machiavelli is simply providing genuine insights into social organization as the foundation for Politics (Lerner, 1950). He is clear and logical. Emotion and ethics are only a small part of Machiavelli’s framework, “Everybody sees what you appear to be, few feel what you are, and those few will not dare oppose themselves to the many, who have the majesty of the state to defend them” (Santoni, 123). Machiavelli provides guidance for leaders for tasks such as dealing with newly acquired territory, choosing administrators, how to conduct diplomacy, and warfare (Lerner, 1950).
Machiavelli gives specific examples of the way to govern newly acquired territory. He uses various situations by which a Prince could acquire new territory and how he should govern the territory. Machiavelli is sensitive to the principles of the people of the newly acquired territory. He acknowledges that the people will overthrow the leader if he crosses them, “One who by his own valor and measures animates the mass of the people, he will not find himself deceived by them, he will find he has laid his foundations well” (Santoni, 114). To be a Prince you must be feared by your people, but not hated. Hatred will lead to destruction. Machiavelli wants the prince to form an atmosphere in which the people fear him, but also highly respect him (Lerner, 1950). The fear comes from the potential use of force by the Prince’s military against them. Machiavelli argues that a prince’s sole obligation is to protect the nation; a prince is in control of the military and is in charge of national security.
By proving military dominance, you gain power (Lerner, 1950).`

const cleanText = text
    .toLowerCase()
    .split("")
    .filter((char) => char.match(/[a-z ,.]/))
    .join("")

const bigrams = []
for (let i = 0; i < cleanText.length - 1; i++) {
    const bigram = cleanText.slice(i, i + 2)
    if (bigram.match(/[a-z]{2}/)) {
        bigrams.push(bigram)
    }
}

const bigramCounts = countFrequency(bigrams)
const totalBigrams = bigrams.length

const bigramFrequencies = Object.fromEntries(
    Object.entries(bigramCounts)
        .map(([bigram, count]) => [bigram, (count / totalBigrams) * 100])
        .filter((bigram) => bigram[1] > 1)
)
const bigramFrequenciesSorted = Object.fromEntries(Object.entries(bigramFrequencies).sort((a, b) => b[1] - a[1]))

const frequentBigrams = Object.keys(bigramFrequenciesSorted)
const letters = cleanText
    .split("")
    .filter(
        (letter, index) =>
            !(frequentBigrams.includes(letter + cleanText[index + 1]) || frequentBigrams.includes(cleanText[index - 1] + letter) || frequentBigrams.includes(cleanText[index + 1] + letter) || frequentBigrams.includes(letter + cleanText[index - 1]))
    )

const letterCounts = countFrequency(letters)
const totalLetters = letters.length

const letterFrequencies = Object.fromEntries(Object.entries(letterCounts).map(([letter, count]) => [letter, (count / totalLetters) * 100]))
const letterFrequenciesSorted = Object.fromEntries(Object.entries(letterFrequencies).sort((a, b) => b[1] - a[1]))
