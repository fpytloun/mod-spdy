#!/usr/bin/env python

# Copyright (c) 2009 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# Creates chrome_version.cc which contains the definition of the
# kChromeVersion constant.

import sys

def main(me, args):
  if len(args) != 2:
    print >>sys.stderr, 'usage: %s version.cc version' % me
    return 1

  (cc_file, version) = args

  contents = '''// automatically generated by %s

#include "chrome/common/chrome_constants.h"

namespace chrome {

const char kChromeVersion[] = "%s";

}  // namespace chrome
''' % (me, version)

  output = open(cc_file, 'w')
  output.write(contents)
  output.close()

  return 0

if __name__ == '__main__':
  sys.exit(main(sys.argv[0], sys.argv[1:]))
