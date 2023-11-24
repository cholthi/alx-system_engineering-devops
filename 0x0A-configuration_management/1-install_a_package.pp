#!/usr/bin/pup
# Install flask with version 2.0.1

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
