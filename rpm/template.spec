%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/eloquent/.*$
%global __requires_exclude_from ^/opt/ros/eloquent/.*$

Name:           ros-eloquent-gmock-vendor
Version:        1.8.9000
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS gmock_vendor package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-eloquent-gtest-vendor
Requires:       ros-eloquent-ros-workspace
BuildRequires:  cmake
BuildRequires:  ros-eloquent-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The package provides GoogleMock.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/eloquent/setup.sh" ]; then . "/opt/ros/eloquent/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/eloquent" \
    -DCMAKE_PREFIX_PATH="/opt/ros/eloquent" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/eloquent/setup.sh" ]; then . "/opt/ros/eloquent/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/eloquent

%changelog
* Wed Jan 29 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.8.9000-1
- Autogenerated by Bloom

