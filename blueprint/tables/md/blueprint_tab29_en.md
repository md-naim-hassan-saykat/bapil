**Table 29.** Model selection criteria and weights

| Criterion | Weight | Evidence |
|--------------------------|--------|------------------------------------|
| Bangla and English quality on BanglaPolicyQA | 30% | Retrieval and answer metrics of Table 28 on the frozen benchmark |
| Faithfulness to cited sources | 20% | Citation precision and unsupported-claim rate |
| Safety and robustness | 15% | Red-team results; prompt-injection success rate; refusal behaviour |
| Deployability on local hardware | 15% | Memory and latency at the target quantisation on pilot GPUs |
| Licence and openness | 10% | Licence terms; availability of weights; usage restrictions |
| Transparency and documentation | 10% | Model card quality; training-data disclosure [50] |

*Note.* A model that fails any safety threshold in Table 28 is excluded regardless of its total score.
