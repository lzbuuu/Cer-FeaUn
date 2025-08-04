# Cer-FeaUn: Certified Feature Unlearning in Vertical Federated Learning
In this paper, we proposed Cer-FeaUn, a certified feature unlearning, trading off between the overheads and accuracy. Specifically, a novel feature perturbation strategy is first proposed to construct a perturbed dataset, where the sensitive features are perturbed with noises. Then, the effect is defined as the parameters difference between models trained with the original and perturbed dataset. Finally, an unlearned model is trained in first-order, where the effect is removed from the original model in one epoch. Furthermore, Cer-FeaUn performs certified removal for server-side models with strongly convex loss functions. That is, the distribution of the unlearned model is statistically indistinguishable from that of the retrained model. For the scenario with a few sensitive features, simulation results show that the accuracy of the unlearned model is up to 84.79%, and the runtime of Cer-FeaUn is 15 times faster than that of the retrained model.

# Architecture
The Framework of Cer-FeaUn. Cer-FeaUn requires only one epoch, which consists of six steps: (a) active clients perturb their own datasets using the feature perturbation strategy, (b) all clients input the dataset into the client-side model, (c) the outputs of client-side models are uploaded to server, (d) server evaluate the association between the sensitive features and the model, (e) server download modified gradients, (f) all clients update model using corresponding gradient.
![fram1 (1)](./Cer-FeaUn.pdf)

# Citation
@article{wang2025cer,
  title={Cer-FeaUn: Certified Feature Unlearning in Vertical Federated Learning},
  author={Wang, Yilei and Lu, Zhaobo and Liu, Zhiquan and Li, Tao and Chen, Zhenhua and Susilo, Willy},
  journal={IEEE Transactions on Mobile Computing},
  number={01},
  pages={1--13},
  year={2025},
  publisher={IEEE Computer Society}
}

