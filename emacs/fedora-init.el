;; $Id: fedora-init.el,v 1.3 2003/12/06 22:46:06 scop Exp $

(defun fedora-new-rpm-spec-file-init ()
  (delete-region (point-min) (point-max))
  (set (make-local-variable 'indent-tabs-mode) nil)
  (set (make-local-variable 'buffer-file-coding-system) 'utf-8)
  (if buffer-file-name
      (let* ((pkgname
              (file-relative-name
               (file-name-sans-extension buffer-file-name)))
             (cpandist
              (if (string-match "^perl-\\(.*\\)$" pkgname)
                  (match-string 1 pkgname) nil)))
        (if cpandist
            (insert-file-contents "/usr/share/fedora/spectemplate-perl.spec")
          (insert-file-contents "/usr/share/fedora/spectemplate-minimal.spec"))
        (goto-char (point-min))
        (and (re-search-forward "^\\(Name:\\s-*\\).*$" nil t)
             (replace-match (concat (match-string 1) pkgname) t))
        (when cpandist
          (goto-char (point-min))
          (and (re-search-forward "^\\(URL:\\s-*\\).*$" nil t)
               (replace-match (concat (match-string 1)
                                      "http://search.cpan.org/dist/"
                                      cpandist "/") t))
          (goto-char (point-min))
          (and (re-search-forward "^\\(%setup\\s-+-q\\).*$" nil t)
               (replace-match (concat (match-string 1)
                                      " -n " cpandist "-%{version}") t))))
    (insert-file-contents "/usr/share/fedora/spectemplate-minimal.spec"))
  (goto-char (point-min))
  (re-search-forward "^[A-Za-z]+:\\s-*$" nil t)
  (set-buffer-modified-p nil))

(remove-hook 'rpm-spec-mode-new-file-hook 'rpm-spec-initialize)
(add-hook 'rpm-spec-mode-new-file-hook 'fedora-new-rpm-spec-file-init t)
