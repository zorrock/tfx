# Copyright 2019 Google LLC. All Rights Reserved.
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
"""TFX ImportExampleGen component definition."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from typing import Optional, Text

from tfx.components.base import base_component
from tfx.components.example_gen import component
from tfx.components.example_gen.import_example_gen import executor
from tfx.proto import example_gen_pb2
from tfx.utils import channel


class ImportExampleGen(component.ExampleGen):
  """Official TFX ImportExampleGen component.

  The ImportExampleGen component takes TFRecord files with TF Example data
  format, and generates train and eval examples for downsteam components.
  This component provides consistent and configurable partition, and it also
  shuffle the dataset for ML best practice.

  Args:
    input_base: A Channel of 'ExternalPath' type, which includes one artifact
      whose uri is an external directory with TFRecord files inside.
    input_config: An example_gen_pb2.Input instance, providing input
      configuration. If unset, the files under input_base will be treated as a
      single split.
    output_config: An example_gen_pb2.Output instance, providing output
      configuration. If unset, default splits will be 'train' and 'eval' with
      size 2:1.
    name: Optional unique name. Necessary if multiple ImportExampleGen
      components are declared in the same pipeline.
    outputs: Optional dict from name to output channel.
  Attributes:
    outputs: A ComponentOutputs including following keys:
      - examples: A channel of 'ExamplesPath' with train and eval examples.
  """

  def __init__(self,
               input_base: channel.Channel,
               input_config: Optional[example_gen_pb2.Input] = None,
               output_config: Optional[example_gen_pb2.Output] = None,
               name: Optional[Text] = None,
               outputs: Optional[base_component.ComponentOutputs] = None):
    super(ImportExampleGen, self).__init__(
        executor=executor.Executor,
        input_base=input_base,
        input_config=input_config,
        output_config=output_config,
        component_name='ImportExampleGen',
        unique_name=name,
        outputs=outputs)
