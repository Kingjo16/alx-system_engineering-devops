#!/usr/bin/pup
# Install an especific version of flsk package with pip3 (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
