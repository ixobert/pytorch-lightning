# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import torch


class NativeAMP:

    def __init__(self, trainer):
        self.trainer = trainer

    def connect(self, model, optimizers):
        self.trainer.optimizers = optimizers
        return model, optimizers

    def training_step(self, fx, args):
        with torch.cuda.amp.autocast():
            output = fx(*args)
        return output
